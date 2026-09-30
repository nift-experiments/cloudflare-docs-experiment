<p class="article-summary">Create an origin rule to change the HTTP `Host` header and DNS record.</p>
<p>The following origin rule overrides the HTTP <code>Host</code> header to <code>hr-server.example.com</code> for all requests with a URI path starting with <code>/hr-app/</code>. It also overrides the DNS record to the same hostname.</p>
<p>The <code>Host</code> header override only updates the header value; the DNS record override will handle the rerouting of incoming requests. For more information on these overrides, refer to <a href="/rules/origin-rules/features/">Origin Rules settings</a>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13091.md")
</div></div>
