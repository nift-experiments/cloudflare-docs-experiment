<p>Gateway supports creating <a href="/cloudflare-one/reusable-components/lists/">lists</a> of IPs, hostnames, or other entries to reference in your policies.</p>
<p>It is likely that you will be onboarding to the Cloudflare platform with some predetermined series of security policies. Maybe you have explicit deny lists based on hostnames, IPs, or another measure that tie to individual users. Maybe some networks can access certain apex records while others cannot.</p>
<p>The best way to migrate to Cloudflare in a way that will simplify ongoing maintenance is to build as many reusable objects as possible. Not only because that makes policy building simpler, but because as those applications, networks, and services organically change and grow, updates to the lists automatically update everywhere that the lists are applied.</p>
<h2 id="create-a-list-from-a-csv-file">Create a list from a CSV file</h2>
<p>To test uploading CSV lists, you can download a <a href="/cloudflare-one/static/list-test.csv">sample CSV file</a> of IP address ranges or copy the following into a file:</p>
<pre><code class="language-csv">value,description&#10;192.0.2.0/24,This is an IP address range in CIDR format&#10;198.51.100.0/24,This is also an IP address range&#10;203.0.113.0/24,This is the third IP address range&#10;</code></pre>
<p>When you format a CSV file for upload:</p>
<ul>
<li>Each line should be a single entry that includes a value and an optional description.</li>
<li>A header row must be present for Zero Trust to recognize descriptions.</li>
<li>Trailing whitespace characters are not allowed.</li>
<li>CRLF (Windows) and LF (Unix) line endings are valid.</li>
</ul>
<p>To upload the list to the Cloudflare dashboard:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10032.md")
</div></div>
<p>You can now use this list in the policy builder by choosing the <em>in list</em> operator.</p>
<h2 id="create-a-list-manually">Create a list manually</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10036.md")
</div></div>
<p>You can now use this list in the policy builder by choosing the <em>in list</em> operator.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="create-lists-in-advance">Create lists in advance</h3>
@markup("md", "content/.markup/bodies/10029.md")
</aside>
