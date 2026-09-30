<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13093.md")
</aside>
<h2 id="why-is-a-page-rule-not-working">Why is a page rule not working?</h2>
<p>The most common reason that a page rule is not working — such as URL forwarding — is that the page rule you created is on a record that is not proxied by Cloudflare in your <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS settings</a>.</p>
<p>Consider an example where you have a page rule that redirects a subdomain (<code>subdomain.yoursitename.com</code>) back to your apex domain (<code>yoursitename.com</code>). If you do not have that record proxied in your DNS settings for the subdomain record, Cloudflare's proxy is not running over the record and a page rule will not work because it is going direct to your server.</p>
<h2 id="error-500-internal-server-error">Error 500 (Internal server error)</h2>
<h3 id="root-cause">Root cause</h3>
<p>This may be due to a configuration issue on a page rule. When creating a page rule that uses two wildcards, like a <em>Forwarding URL</em> rule, it is possible to create a rule that mentions the second wildcard with the <code>$2</code> placeholder. Refer to the example below:</p>
<p><img src="/assets/upstream/images/support/page-rule-create.png" alt="Example Page Rule configuration with two wildcards. The forwarding URL contains a $2 placeholder, which will be replaced with the content matched by the second " /></p>
<p>When updating the same rule, you can remove one of the wildcard in the <strong>If the URL matches</strong> field and save it. Refer to the example below:</p>
<p><img src="/assets/upstream/images/support/page-rule-update.png" alt="Incorrect Page Rule configuration with a single wildcard, but still using the $2 placeholder in the forwarding URL. This configuration causes " /></p>
<p>If you do so, the <code>$2</code> placeholder reference a wildcard that does not exist anymore, and as such, an <code>Error 500 (Internal server error)</code> is thrown when a URL triggers the page rule.</p>
<h3 id="resolution">Resolution</h3>
<p>Update the page rule and remove the reference <code>$2</code> to the second wildcard. If there is only one wildcard, then you can only use <code>$1</code>.</p>
