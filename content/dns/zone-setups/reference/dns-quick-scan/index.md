<p>To help all customers get started when a new zone is created, Cloudflare offers a DNS records quick scan.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="where-to-find-the-quick-scan">Where to find the quick scan</h3>
@markup("md", "content/.markup/bodies/7913.md")
</aside>
<h2 id="how-quick-scan-works">How quick scan works</h2>
<p>The scan is built upon a list of recurring patterns of DNS records <strong>Type</strong> and <strong>Name</strong>, that Cloudflare identifies as being used in existing active zones.</p>
<p>Since DNS record names are automatically appended with the domain that the records are set for, two completely different domains - <code>example.com</code> and <code>domain.test</code>, for example - would probably have a few matches if the lists of DNS records on their zones were compared side by side and the criterion was <strong>Type</strong>/<strong>Name</strong> combination.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@input("content/.markup/bodies/7916.md")
</div></details>
<p>The DNS records <strong>Content</strong> would be different for each zone but, based on record <strong>Type</strong> and <strong>Name</strong>, Cloudflare can identify recurring patterns and expect to find the same pairs when a new domain is added.</p>
<p>The <a href="#use-case-examples">use cases section</a> below provides some examples of DNS records <strong>Type</strong>/<strong>Name</strong> combinations that the scan usually finds.</p>
<h2 id="limitations">Limitations</h2>
<p>Since the DNS records quick scan is not tailored to the specific zone you are adding to Cloudflare, there can be cases where not all records are picked up.</p>
<p>For example, if you have very specific hostnames - such as <code>my-store1900.example.com</code> instead of <code>store.example.com</code> - or if you have set up a <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DKIM record</a> that uses a more custom name - <code>this._domainkey</code> instead of <code>default._domainkey</code> - it is expected that the scan will not find the specific DNS records.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7912.md")
</aside>
<h2 id="use-case-examples">Use case examples</h2>
<h3 id="address-records">Address records</h3>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7917.md")
</div>
<p>The value <code>@</code> indicates the domain apex - in the example above, <code>domain.test</code> or <code>example.com</code>.</p>
<p>Virtually all zones on a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a> are expected to have at least one <a href="https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/">address record</a> pointing to the IP address where the website or application is hosted.</p>
<h3 id="www-records">www records</h3>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/7918.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@input("content/.markup/bodies/7919.md")
</div>
<p>Since it is still common that visitors type <code>www.&lt;DOMAIN&gt;</code> in their browsers expecting to reach the domain, zones will usually have a  <a href="/dns/manage-dns-records/reference/dns-record-types/#cname">CNAME</a> or an <a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa">A</a> record named <code>www</code>. This allows queries for <code>www.&lt;DOMAIN&gt;</code> to return the expected result.</p>
<h3 id="email-records">Email records</h3>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@input("content/.markup/bodies/7920.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-4">Example</h3>
@input("content/.markup/bodies/7921.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-5">Example</h3>
@input("content/.markup/bodies/7922.md")
</div>
<p>Mail exchanger (<code>MX</code>) and other record types combined with names like <code>mail</code>, <code>webmail</code>, or <code>smtp</code>, are also commonly found. As explained in the <a href="/dns/manage-dns-records/how-to/email-records/">Set up email records page</a>, there are several DNS records that can be used to make sure email reaches your mail server and to prevent other email senders from spoofing your domain.</p>
