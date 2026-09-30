<p>When you add an <code>NS</code> record to your zone, you create a <strong>subdomain delegation</strong>: you delegate authority for that subdomain (and everything below it) to another set of nameservers. Any record you keep at or below that delegation point is <strong>shadowed</strong>. It stays stored in your zone, but the delegation places authority for that name with the delegated nameservers, so the record is not part of the authoritative data your zone is meant to serve.</p>
<p>Shadow metadata tells you which records are shadowed, which <code>NS</code> records do the shadowing, and how many records each delegation shadows. It is exposed as fields on API responses and as warnings in the Cloudflare dashboard, and is not returned unless you explicitly request it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7793.md")
</aside>
<h2 id="why-shadowed-records-matter">Why shadowed records matter</h2>
<p>Because a delegation moves authority for a subdomain elsewhere, any record you place at or below it is not authoritative, even though it still appears in your zone. Consider this example:</p>
<pre><code class="language-txt">sub.example.com      NS  ns1.example.org.&#10;www.sub.example.com  A   192.0.2.1&#10;</code></pre>
<p>The <code>NS</code> delegation at <code>sub.example.com</code> delegates authority for everything at or below it, including <code>www.sub.example.com</code>, to the external nameservers. Those nameservers, not your zone, are responsible for answering that name, so the <code>A</code> record you added here is not the authoritative record for <code>www.sub.example.com</code>.</p>
<p>The problem works in both directions. Adding an <code>NS</code> delegation can shadow records you already depend on, and adding records under an existing delegation produces records your zone is no longer authoritative for. In both cases no error is returned, which is what makes shadow metadata useful for spotting the issue.</p>
<p>Shadowed records arise in exactly two ways:</p>
<ul>
<li>You added a delegation over records that already existed at or below that name, for example when you point a subdomain at an external provider but leave the original records in place.</li>
<li>You added records at or below a name that was already delegated, for example expecting them to resolve from the parent zone.</li>
</ul>
<h2 id="glue-records">Glue records</h2>
<p>A glue record is an <code>A</code> or <code>AAAA</code> record that some delegations need in order to work. Glue is required only when a delegation's nameserver hostname falls within the delegated zone itself. Most delegations point at nameservers in a different zone (for example, <code>ns1.example.org</code> for a delegation of <code>sub.example.com</code>) and need no glue, because the resolver can look those nameservers up independently. Without glue in the in-zone case, a resolver asking &quot;where is <code>ns1.sub.example.com</code>?&quot; would follow the delegation for <code>sub.example.com</code> — which it cannot reach until it already knows <code>ns1.sub.example.com</code>. This is a circular dependency.</p>
<p>Consider this example:</p>
<pre><code class="language-txt">sub.example.com      NS  ns1.sub.example.com.&#10;ns1.sub.example.com  A   192.0.2.1&#10;</code></pre>
<p>The <code>A</code> record for <code>ns1.sub.example.com</code> is glue. It is shadowed (the <code>sub.example.com</code> delegation takes effect first), but it is still served. The parent zone includes it in the additional section of the referral response, alongside the <code>NS</code> delegation, so resolvers can bootstrap the subdomain lookup without getting stuck in a circular dependency.</p>
<p>Glue is only meaningful for <code>A</code> and <code>AAAA</code> records. A <code>CNAME</code> record at the same name as an <code>NS</code> target is not treated as glue.</p>
<h2 id="unreachable-glue-records">Unreachable glue records</h2>
<p>A glue record becomes unreachable when a shallower delegation takes authority for the name the glue is meant to support. The shallower delegation (one closer to the zone apex, with fewer labels in its name) takes authority for everything below it, so your zone cannot serve the glue even in the additional section of a referral. The API reports these records with <code>dead_glue: true</code>.</p>
<p>Consider this example:</p>
<pre><code class="language-txt">sub.example.com        NS  ns1.sub.example.com.&#10;a.sub.example.com      NS  ns1.a.sub.example.com.&#10;ns1.a.sub.example.com  A   192.0.2.1&#10;</code></pre>
<p>The <code>A</code> record for <code>ns1.a.sub.example.com</code> looks like glue for the <code>a.sub</code> delegation. However, the shallower <code>sub.example.com</code> delegation takes authority for everything under <code>sub.example.com</code>, including <code>a.sub.example.com</code>. Your zone's authority stops at that shallower delegation, so the glue for <code>ns1.a.sub.example.com</code> is outside it and is never served.</p>
<p>Unreachable glue does not cause resolution failures. It is either a leftover you can safely remove, or a signal that the shallower delegation was created in error.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7792.md")
</aside>
<h2 id="shadow-metadata-fields">Shadow metadata fields</h2>
<p>Shadow metadata fields are returned in each record's <code>meta</code> object when applicable. They are computed on demand at read time and are never stored.</p>
<h3 id="shadowed-by"><code>shadowed_by</code></h3>
<p>Type: array of strings (record IDs)</p>
<p>Present on any record that is hidden by one or more <code>NS</code> delegations. The array contains the IDs of the <code>NS</code> records whose delegations shadow this record. Multiple IDs appear when several <code>NS</code> records share the same delegation name, or when delegations exist at more than one parent level above the record.</p>
<p><code>shadowed_by</code> is always present on glue records, because glue records are shadowed by definition.</p>
<p>Apex records (records whose name equals the zone name) are never shadowed and never carry this field.</p>
<p>An <code>NS</code> record at the same name as a delegation is not considered shadowed by that delegation — it is the delegation. It can carry <code>shadowed_by</code> only when a delegation exists at a shallower parent level.</p>
<h3 id="is-glue"><code>is_glue</code></h3>
<p>Type: boolean</p>
<p>Present and set to <code>true</code> on <code>A</code> or <code>AAAA</code> records whose name matches the target of one of the <code>NS</code> records that shadows them. These records are required glue for the delegation. Even though they are shadowed, they are still served: the parent zone includes them in the additional section of referral responses so resolvers can reach the delegated nameservers.</p>
<p>This field is omitted when the record is not glue.</p>
<h3 id="dead-glue"><code>dead_glue</code></h3>
<p>Type: boolean</p>
<p>Present and set to <code>true</code> on glue records that are never actually served, because a shallower delegation intercepts authority before the zone can answer for that name. A record with <code>dead_glue: true</code> also carries <code>is_glue: true</code>.</p>
<p>This field is omitted when the record is live glue or is not glue at all.</p>
<h3 id="shadowed-records-count"><code>shadowed_records_count</code></h3>
<p>Type: integer</p>
<p>Present on non-apex <code>NS</code> records that form a delegation. Reports how many records in the zone are shadowed by that delegation (records at or below the delegation name, excluding the delegation's own <code>NS</code> records and hidden records).</p>
<p>The count is capped at 10,000. A value of 10,000 means &quot;at least 10,000&quot;. The field is omitted when the count is zero.</p>
<p>The following table shows which shadow metadata fields apply to each record type:</p>
<table>
<thead>
<tr>
<th>Record type</th>
<th><code>shadowed_by</code></th>
<th><code>is_glue</code></th>
<th><code>dead_glue</code></th>
<th><code>shadowed_records_count</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>A</code></td>
<td>Yes, if below a delegation</td>
<td>Yes, if name matches NS target</td>
<td>Yes, if glue and a shallower delegation intercepts authority</td>
<td>No</td>
</tr>
<tr>
<td><code>AAAA</code></td>
<td>Yes, if below a delegation</td>
<td>Yes, if name matches NS target</td>
<td>Yes, if glue and a shallower delegation intercepts authority</td>
<td>No</td>
</tr>
<tr>
<td><code>NS</code> (apex)</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td><code>NS</code> (non-apex, at delegation name)</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td><code>NS</code> (non-apex, below a delegation)</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<td><code>CNAME</code>, <code>MX</code>, <code>TXT</code>, <code>SRV</code>, <code>CAA</code>, <code>HTTPS</code>, <code>SVCB</code></td>
<td>Yes, if below a delegation</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="request-shadow-metadata">Request shadow metadata</h2>
<p>Add <code>include_shadow_metadata=true</code> to any DNS records API request:</p>
<pre><code class="language-sh">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?include_shadow_metadata=true&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Shadow metadata is available on all record API responses: individual record reads, create and update responses, list requests, and batch requests. For list and batch requests, shadow metadata is computed only when the page or batch contains 1,000 records or fewer. Requests above that limit return records without shadow metadata.</p>
<h3 id="find-records-shadowed-by-a-delegation">Find records shadowed by a delegation</h3>
<p>To list only the records shadowed by a specific delegation, pass <code>shadowed_by_name</code> together with <code>include_shadow_metadata=true</code>:</p>
<pre><code class="language-sh">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?include_shadow_metadata=true&amp;shadowed_by_name=sub.example.com&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>The value must be a subdomain of the zone (not the zone apex). The filter returns all records at or below that name. The <code>NS</code> records at exactly the delegation name are excluded (they form the delegation, not the shadowed set). <code>NS</code> records at names below the delegation — for example, a further delegation at <code>a.sub.example.com</code> when filtering by <code>sub.example.com</code> — are themselves shadowed and are included.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7791.md")
</aside>
<h3 id="find-delegations-shadowing-a-record">Find delegations shadowing a record</h3>
<p>To find the <code>NS</code> delegations that shadow a specific record, pass <code>shadowing_name</code>:</p>
<pre><code class="language-sh">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?shadowing_name=www.sub.example.com&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>The filter returns <code>NS</code> records at the provided name and at each of its ancestor names within the zone, excluding the zone apex. In this example, the API searches for <code>NS</code> records at <code>www.sub.example.com</code> and <code>sub.example.com</code>. The value must be a subdomain of the zone (not the zone apex).</p>
<p>Unlike <code>shadowed_by_name</code>, this filter does not require <code>include_shadow_metadata=true</code>.</p>
<h2 id="example-response">Example response</h2>
<p>The following is an excerpt showing shadow metadata fields on three records in a zone containing:</p>
<pre><code class="language-txt">sub.example.com       NS    ns1.sub.example.com.&#10;ns1.sub.example.com   A     192.0.2.1&#10;www.sub.example.com   A     192.0.2.2&#10;</code></pre>
<pre><code class="language-json">[&#10;  {&#10;    &quot;type&quot;: &quot;NS&quot;,&#10;    &quot;name&quot;: &quot;sub.example.com&quot;,&#10;    &quot;content&quot;: &quot;ns1.sub.example.com.&quot;,&#10;    &quot;meta&quot;: {&#10;      &quot;shadowed_records_count&quot;: 2&#10;    }&#10;  },&#10;  {&#10;    &quot;type&quot;: &quot;A&quot;,&#10;    &quot;name&quot;: &quot;ns1.sub.example.com&quot;,&#10;    &quot;content&quot;: &quot;192.0.2.1&quot;,&#10;    &quot;meta&quot;: {&#10;      &quot;shadowed_by&quot;: [&quot;&lt;NS_RECORD_ID&gt;&quot;],&#10;      &quot;is_glue&quot;: true&#10;    }&#10;  },&#10;  {&#10;    &quot;type&quot;: &quot;A&quot;,&#10;    &quot;name&quot;: &quot;www.sub.example.com&quot;,&#10;    &quot;content&quot;: &quot;192.0.2.2&quot;,&#10;    &quot;meta&quot;: {&#10;      &quot;shadowed_by&quot;: [&quot;&lt;NS_RECORD_ID&gt;&quot;]&#10;    }&#10;  }&#10;]&#10;</code></pre>
<p>The <code>NS</code> record carries <code>shadowed_records_count: 2</code> (two records are shadowed by it). The glue <code>A</code> record carries both <code>shadowed_by</code> and <code>is_glue: true</code>. The non-glue <code>A</code> record carries only <code>shadowed_by</code>.</p>
