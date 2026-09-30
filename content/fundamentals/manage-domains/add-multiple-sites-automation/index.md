<p>To add multiple sites to Cloudflare at once and more efficiently, you can do so via the Cloudflare API.</p>
<p>Adding multiple sites can be useful when you:</p>
<ul>
<li>Have multiple domains mapping back to a single, canonical domain (common for domains in different countries - such as <code>.com.au</code>, <code>.co.uk</code> - that you want protected by Cloudflare).</li>
<li>Are a <a href="https://www.cloudflare.com/partners/">partner</a>, agency, or IT consultancy, and manage multiple domains on behalf of your customers.</li>
<li>Are moving an existing set of sites over to Cloudflare.</li>
</ul>
<p>Using the API will allow you to add multiple sites quickly and efficiently, especially if you are already familiar with <a href="/dns/zone-setups/full-setup/setup/">how to change your nameservers</a> or <a href="/dns/manage-dns-records/how-to/create-dns-records/">add a DNS record</a>.</p>
<p>This tutorial assumes domains will be added using a <a href="/dns/zone-setups/full-setup/">primary DNS setup (full)</a>.</p>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<p>To add multiple sites to Cloudflare via automation, you need:</p>
<ul>
<li>An existing <a href="/fundamentals/account/create-account/">Cloudflare account</a>.</li>
<li>Command line with <code>curl</code></li>
<li>A Cloudflare <a href="/fundamentals/api/get-started/create-token/">API token</a> with one of the following permissions:
<ul>
<li>Zone-level <code>Administrator</code></li>
<li>Zone-level <code>Zone: Edit</code> and <code>DNS: Edit</code></li>
<li>Account-level <code>Domain Administrator</code></li>
</ul>
</li>
<li>To have disabled <a href="/dns/concepts/#dnssec">DNSSEC</a> for each domain at your registrar (where you bought your domain name).</li>
</ul>
<details class="nb-details"><summary>Provider-specific DNSSEC instructions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/8923.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8922.md")
</aside>
<hr />
<h2 id="1-add-domains"><ol>
<li>Add domains</li>
</ol></h2>
<ol>
<li>Create a list of domains you want to add, each on a separate line (newline separated), stored in a file such as <code>domains.txt</code>.</li>
<li>Create a bash script <code>add-multiple-zones.sh</code> and add the following. Add <code>domains.txt</code> to the same directory or update its path accordingly.</li>
</ol>
<pre><code class="language-bash">  for domain in $(cat domains.txt); do&#10;    printf &quot;Adding ${domain}:\n&quot;&#10;&#10;    curl https://api.cloudflare.com/client/v4/zones \&#10;    &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;    &#45;-header &quot;Content-Type: application/json&quot; \&#10;    &#45;-data &#x27;{&#10;      &quot;account&quot;: {&#10;        &quot;id&quot;:&quot;&lt;ACCOUNT_ID&gt;&quot;&#10;      },&#10;      &quot;name&quot;: &quot;&#x27;&quot;$domain&quot;&#x27;&quot;,&#10;      &quot;type&quot;: &quot;full&quot;&#10;    }&#x27;&#10;&#10;    printf &quot;\n\n&quot;&#10;  done&#10;</code></pre>
<ol start="3">
<li>Open the command line and run:</li>
</ol>
<pre><code class="language-sh">bash add-multiple-zones.sh&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8921.md")
</aside>
<p>After adding a domain, it will be in a <a href="/dns/zone-setups/reference/domain-status/"><code>Pending Nameserver Update</code></a> state.</p>
<h3 id="additional-options">Additional options</h3>
<h4 id="jq">jq</h4>
<p><a href="https://jqlang.github.io/jq/"><code>jq</code></a> is a command-line tool that parses and beautifies JSON outputs.</p>
<p>This tool is a requirement to complete any additional option steps in this tutorial.</p>
<pre><code class="language-sh">echo &#x27;{&quot;foo&quot;:{&quot;bar&quot;:&quot;foo&quot;,&quot;testing&quot;:&quot;hello&quot;}}&#x27; | jq .&#10;</code></pre>
<p>Refer to <code>jq</code> <a href="https://jqlang.github.io/jq/manual/#basic-filters">documentation</a> for more information.</p>
<h4 id="quick-scan">Quick scan</h4>
<p>Cloudflare offers a <a href="/dns/zone-setups/reference/dns-quick-scan/">quick scan</a> that helps populate a zone's DNS records. This scan is a best effort attempt based on a predefined list of commonly used record names and types.</p>
<p>This API call requires the domain ID. This can be found in the following locations:</p>
<ul>
<li><a href="/api/resources/zones/methods/create/#Request">Create Zone</a></li>
<li><a href="/api/resources/zones/methods/list/">List Zones</a></li>
</ul>
<p>Using <code>jq</code> with the first option above, modify your script <code>add-multiple-zones.sh</code> to extract the domain ID and run a subsequent API call to quick scan DNS records.</p>
<pre><code class="language-js">  for domain in $(cat domains.txt); do&#10;    printf &quot;Adding ${domain}:\n&quot;&#10;&#10;    add_output=`curl https://api.cloudflare.com/client/v4/zones \&#10;      &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;      &#45;-header &quot;Content-Type: application/json&quot; \&#10;      &#45;-data &#x27;{&#10;        &quot;account&quot;: {&#10;          &quot;id&quot;:&quot;&lt;ACCOUNT_ID&gt;&quot;&#10;        },&#10;        &quot;name&quot;: &quot;&#x27;&quot;$domain&quot;&#x27;&quot;,&#10;        &quot;type&quot;: &quot;full&quot;&#10;      }&#x27;`&#10;&#10;    echo $add_output | jq .&#10;&#10;    domain_id=`echo $add_output | jq -r .result.id`&#10;&#10;    printf &quot;\n\n&quot;&#10;    printf &quot;DNS quick scanning ${domain}:\n&quot;&#10;&#10;    scan_output=`curl --request POST https://api.cloudflare.com/client/v4/zones/$domain_id/dns_records/scan \&#10;      &#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;      &#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;`&#10;&#10;    echo $scan_output | jq .&#10;&#10;  done&#10;</code></pre>
<h2 id="2-update-nameservers"><ol start="2">
<li>Update nameservers</li>
</ol></h2>
<p>For each domain to become active on Cloudflare, it must be activated in either <a href="/dns/zone-setups/full-setup/setup/">Full setup</a> or <a href="/dns/zone-setups/partial-setup/setup/">Partial setup</a>. The following script will output a list containing the nameservers associated with each domain.</p>
<p>You can find your zones nameservers in the following locations:</p>
<ul>
<li><a href="/api/resources/zones/methods/create/#Request">Create Zone</a></li>
<li><a href="/api/resources/zones/methods/get/">Zone Details</a></li>
</ul>
<ol>
<li>Modify your script <code>add-multiple-zones.sh</code> to print a CSV with data from the <code>Create Zone</code> JSON response.</li>
</ol>
<pre><code class="language-js">  for domain in $(cat domains.txt); do&#10;    printf &quot;Adding ${domain}:\n&quot;&#10;&#10;    add_output=`curl https://api.cloudflare.com/client/v4/zones \&#10;      &#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;      &#45;-header &quot;Content-Type: application/json&quot; \&#10;      &#45;-data &#x27;{&#10;        &quot;account&quot;: {&#10;          &quot;id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;        },&#10;        &quot;name&quot;: &quot;&#x27;&quot;$domain&quot;&#x27;&quot;,&#10;        &quot;type&quot;: &quot;full&quot;&#10;      }&#x27;`&#10;&#10;    &#35; Create csv of nameservers&#10;    echo $add_output | jq -r &#x27;[.result.name,.result.id,.result.name_servers[]] | @csv&#x27; &gt;&gt; /tmp/domain_nameservers.csv&#10;&#10;    domain_id=`echo $add_output | jq -r .result.id`&#10;&#10;    printf &quot;\n\n&quot;&#10;    printf &quot;DNS quick scanning ${domain}:\n&quot;&#10;&#10;    scan_output=`curl --request POST https://api.cloudflare.com/client/v4/zones/$domain_id/dns_records/scan \&#10;      &#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;      &#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;`&#10;&#10;    echo $scan_output | jq .&#10;&#10;  done&#10;&#10;  printf &quot;name_servers are saved in /tmp/domain_nameservers&quot;&#10;  cat /tmp/domain_nameservers.csv&#10;</code></pre>
<table>
<thead>
<tr>
<th>ID</th>
<th>ZONE</th>
<th>NAME SERVERS</th>
</tr>
</thead>
<tbody>
<tr>
<td>&lt;ZONE_ID&gt;</td>
<td><code>example.com</code></td>
<td><code>arya.ns.cloudflare.com</code>, <code>tim.ns.cloudflare.com</code></td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Use the values in the <strong>NAME SERVERS</strong> column to <a href="/dns/zone-setups/full-setup/setup/#34-update-your-registrar">update the nameservers</a> at the registrar of each domain.</li>
</ol>
<hr />
<h2 id="limitations">Limitations</h2>
<p>There are limitations on the number of domains you can add at a time - specifically, you can only sign up a maximum of 25 domains every 10 minutes.</p>
<p>In addition, if you have over 50 domains and, of those domains, more are pending than active, you will be blocked from adding more. We recommend waiting until your pending sites have been activated before adding more.</p>
<h2 id="common-issues">Common issues</h2>
<p>If any errors were returned in this process, the domain may not be registered (or only just registered), be a subdomain, or be otherwise invalid. For more details, refer to <a href="/dns/zone-setups/troubleshooting/cannot-add-domain/">Cannot add domain</a>.</p>
