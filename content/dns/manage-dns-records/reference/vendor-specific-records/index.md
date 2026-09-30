<p>This article requires prior knowledge of DNS record management via the Cloudflare dashboard. To learn more, refer to Cloudflare's article on <a href="/dns/manage-dns-records/how-to/create-dns-records/">managing DNS records</a>.</p>
<h2 id="google">Google</h2>
<h3 id="google-workspace-mx-records">Google Workspace MX records</h3>
<p>Google Workspace requires <a href="https://support.google.com/a/answer/174125">specific MX records</a> added to your DNS provider.</p>
<p>Once you <a href="/dns/manage-dns-records/how-to/create-dns-records/">add these records to Cloudflare</a>:</p>
<ul>
<li><a href="https://toolbox.googleapps.com/apps/checkmx/check">Test the configuration</a></li>
<li>Do not add other <code>MX</code> records other than those provided by Google.</li>
</ul>
<h3 id="google-workspace-service-urls">Google Workspace service URLs</h3>
<p>If you want to customize the service addresses URLs associated with Google Workspace, refer to <a href="https://support.google.com/a/answer/53340">Google's documentation</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7783.md")
</aside>
<h3 id="google-site-verification">Google site verification</h3>
<p>To add a site verification record in Cloudflare, follow <a href="https://support.google.com/a/answer/7173990">Google's documentation</a>.</p>
<hr />
<h2 id="amazon">Amazon</h2>
<h3 id="amazon-route53">Amazon Route53</h3>
<p>AWS customers must <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-name-servers-glue-records.html">update their domain's nameservers</a> to point to their new Cloudflare nameservers.</p>
<h3 id="amazon-s3-bucket">Amazon S3 bucket</h3>
<p>Find the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html">URL</a> for your bucket.</p>
<p>Then, <a href="/dns/manage-dns-records/how-to/create-dns-records/">create a <code>CNAME</code> record</a> in Cloudflare. For example, if the full host URL of the bucket is <code>files.example.com.s3.amazonaws.com</code>, you would add a <code>CNAME</code> record similar to the following:</p>
<pre><code class="language-txt">files  CNAME  files.example.com.s3.amazonaws.com&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7782.md")
</aside>
<h3 id="amazon-simple-email-service-ses">Amazon Simple Email Service (SES)</h3>
<p>For help setting up DKIM in SES, refer to the <a href="https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html">Amazon documentation</a>.</p>
<h3 id="amazon-elb-configuration">Amazon ELB configuration</h3>
<p>Refer to <a href="http://docs.amazonwebservices.com/ElasticLoadBalancing/latest/DeveloperGuide/using-domain-names-with-elb.html">Amazon's ELB help content</a> for guidance on ELB configuration at Amazon, but generally you should:</p>
<p>Add a <a href="/dns/manage-dns-records/how-to/create-dns-records/"><code>CNAME</code> record</a> to Cloudflare for the hostname you receive from AWS, for example:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@input("content/.markup/bodies/7784.md")
</div>
<h3 id="amazon-amplify">Amazon Amplify</h3>
<p>To use Cloudflare DNS with AWS Amplify, refer to the <a href="https://docs.aws.amazon.com/amplify/latest/userguide/to-add-a-custom-domain-managed-by-a-third-party-dns-provider.html">Amplify help content</a> and follow the instructions for <strong>manual configuration</strong>.</p>
<p>At Cloudflare, you will need at least two <code>CNAME</code> records:</p>
<ul>
<li>A <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/7785.md")
</div> `CNAME` to validate your domain ownership, which should look like the following:
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@input("content/.markup/bodies/7786.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="cname-flattening">CNAME flattening</h3>
@markup("md", "content/.markup/bodies/7781.md")
</aside>
<ul>
<li>One <code>CNAME</code> for the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/7787.md")
</div> (`example.com`) and/or for each of the subdomains (`blog.example.com`) that you want to manage on Cloudflare. For details refer to [Manage DNS records](/dns/manage-dns-records/how-to/create-dns-records/). These records can be proxied.
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@input("content/.markup/bodies/7788.md")
</div>
***
<h2 id="microsoft">Microsoft</h2>
<h3 id="microsoft-365">Microsoft 365</h3>
<p>For information about the records to Microsoft 365, refer to <a href="https://learn.microsoft.com/en-us/microsoft-365/admin/get-help-with-domains/information-for-dns-records">Microsoft's documentation</a>.</p>
<h3 id="microsoft-azure">Microsoft Azure</h3>
<p>Follow Microsoft's instructions on <a href="https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain">configuring Azure DNS settings</a>.</p>
<p>Then, add Azure's required records to <a href="/dns/manage-dns-records/how-to/create-dns-records/">Cloudflare DNS</a>.</p>
<hr />
<h2 id="miscellaneous-vendors">Miscellaneous vendors</h2>
<h3 id="clickfunnels">ClickFunnels</h3>
<p>You can configure Cloudflare to work with ClickFunnels. The process requires updating your Cloudflare DNS settings.</p>
<ul>
<li><a href="https://help.clickfunnels.com/hc/en-us/articles/360005906774-Adding-A-Cloudflare-Subdomain-">Adding a Cloudflare subdomain</a></li>
<li><a href="https://help.clickfunnels.com/hc/en-us/articles/360005906094-Cloudflare-CNAME-Record">Adding a Cloudflare domain</a></li>
</ul>
<h3 id="discourse">Discourse</h3>
<p>To use Discourse with Cloudflare, refer to <a href="https://community.cloudflare.com/t/using-discourse-with-cloudflare-best-practices/602890">Using Discourse with Cloudflare: Best Practices</a>.</p>
<h3 id="forward-email">Forward Email</h3>
<p>To use Cloudflare with Forward Email, refer to <a href="https://forwardemail.net/guides/cloudflare">Forward Email configuration with Cloudflare</a>.</p>
<h3 id="mailchimp">Mailchimp</h3>
<p>For help with Mailchimp, refer to <a href="https://mailchimp.com/help/connect-domain/">Use a custom domain with Mailchimp</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7780.md")
</aside>
<h3 id="ning-custom-domain">Ning custom domain</h3>
<p>For help with Ning, refer to <a href="https://www.ning.com/help/use-your-own-domain-e-g-example-com-for-your-ning-network/">Use a custom domain with Ning</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7779.md")
</aside>
<h3 id="rackspace-cloudfiles">Rackspace CloudFiles</h3>
<p>Configure Rackspace CloudFiles via <em>CNAME record</em>. Consult the <a href="https://docs.rackspace.com/support/how-to/using-cnames-with-cloud-files-containers/">Rackspace documentation</a>.</p>
<p>Refer to Rackspace CloudFiles's documentation to <a href="https://docs.rackspace.com/support/how-to/using-cnames-with-cloud-files-containers/">get a <code>CNAME</code> value</a>, then <a href="/dns/manage-dns-records/how-to/create-dns-records/">add that record within Cloudflare</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7778.md")
</aside>
<h3 id="sendgrid">SendGrid</h3>
<p>Refer to SendGrid's documentation for how to <a href="https://docs.sendgrid.com/ui/sending-email/content-delivery-networks#using-cloudflare">make SendGrid compatible with Cloudflare</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7777.md")
</aside>
<h3 id="smugmug">SmugMug</h3>
<p>For help with SmugMug, refer to <a href="https://www.smugmughelp.com/en/articles/363-use-a-custom-domain">Use a custom domain with SmugMug</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7776.md")
</aside>
<h3 id="squarespace">Squarespace</h3>
<p>First, make sure you <a href="/dns/zone-setups/full-setup/">update your nameservers</a> and your domain is <a href="/dns/zone-setups/reference/domain-status/">active</a>.</p>
<p>Then, set up your Squarespace DNS records:</p>
<ol>
<li>Get your Squarespace DNS information by following <a href="https://support.squarespace.com/hc/articles/213469948">these instructions</a>.</li>
<li>In Cloudflare, <a href="/dns/manage-dns-records/how-to/create-dns-records/">add those records</a>:
<ul>
<li>All <code>A</code> records should be <a href="/dns/proxy-status/">Proxied</a></li>
<li>The <code>CNAME</code> record for <code>www</code> should also be <strong>Proxied</strong>.</li>
<li>The <code>CNAME</code> record for <code>verify.squarespace.com</code> should be <strong>DNS-only</strong>.</li>
</ul>
</li>
<li>If set up properly, your Squarespace DNS Settings page will now indicate that your 'Settings contain problems.' <strong>This is the expected behavior</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/support/hc-import-squarespace_dns_settings-test-2.png" alt="Screenshot of error warnings in squarespace" /></p>
<h4 id="pending-domain-owner-verification">Pending domain owner verification</h4>
<p>The <code>CNAME</code> record you added for <code>verify.squarespace.com</code> should be <strong>DNS-only</strong>.</p>
<p>If you proxy this record, Squarespace will not be able to verify your domain ownership and show you a <code>This website is pending domain owner verification</code> error. To fix the issue, <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">edit</a> the <code>CNAME</code> record and change the <strong>Proxy status</strong> to <strong>DNS-only</strong>.</p>
<h3 id="tumblr-custom-domain">Tumblr custom domain</h3>
<p>Refer to Tumblr's documentation to <a href="https://help.tumblr.com/hc/en-us/articles/231256548-Custom-Domains">get DNS record values</a>. Then, <a href="/dns/manage-dns-records/how-to/create-dns-records/">add records to Cloudflare DNS</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7775.md")
</aside>
<h3 id="unbounce">Unbounce</h3>
<p>Refer to Unbounce's documentation to <a href="https://documentation.unbounce.com/hc/en-us/articles/204011950">get a <code>CNAME</code> value</a>, then <a href="/dns/manage-dns-records/how-to/create-dns-records/">add that record within Cloudflare</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7774.md")
</aside>
<h3 id="wix">Wix</h3>
<p>You can use Cloudflare with <a href="https://www.wix.com/">Wix websites</a>, though your setup needs to be different than with most website builders.</p>
<p>This is because Wix <a href="https://support.wix.com/en/article/request-cloudflare-support">does not support</a> using Cloudflare nameservers (which is the normal part of a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a> or with domains bought through <a href="/registrar/">Cloudflare Registrar</a>).</p>
<h4 id="using-domain-pointing">Using domain pointing</h4>
<p>If you want to manage your DNS through Cloudflare or you bought a domain through <a href="/registrar/">Cloudflare Registrar</a>, you can connect that domain to Wix through <a href="https://support.wix.com/en/article/connecting-a-domain-to-wix-using-the-pointing-method">domain pointing</a>.</p>
<p>This method means your website is using Cloudflare for DNS only, so all your DNS records should be <a href="/dns/proxy-status/#dns-only-records">DNS-only (unproxied)</a>.</p>
<h3 id="wpengine">WPEngine</h3>
<p>For help configuring WPEngine sites, refer to:</p>
<ul>
<li><a href="https://wpengine.com/support/wordpress-best-practice-configuring-dns-for-wp-engine/">Configuring DNS with WPEngine</a></li>
<li><a href="https://wpengine.com/support/cloudflare-best-practices/">Cloudflare best practices</a></li>
</ul>
<h3 id="zoho">Zoho</h3>
<p>To use Cloudflare with Zoho, refer to <a href="https://www.zoho.com/mail/help/adminconsole/cloudflare.html">Zoho configuration with Cloudflare</a>.</p>
