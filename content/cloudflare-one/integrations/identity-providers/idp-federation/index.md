<p>IdP federation allows organizations with multiple Cloudflare accounts to use a single identity provider (IdP) configuration across accounts. Instead of configuring the same IdP (for example, Okta or Entra ID) separately in every account, you configure it once in a source account and share it with the other accounts in your organization.</p>
<p>Each recipient account gets a read-only IdP connection that routes authentication back to the source account through a bridge — a hidden application in the source account that brokers the cross-account login. End users sign in with their existing IdP credentials, and each account's Access policies evaluate the resulting identity just like any other IdP login.</p>
<h2 id="how-it-works">How it works</h2>
<p>Setting up IdP federation is a two-step process:</p>
<ol>
<li><strong>Create a federation grant.</strong> A grant permits an IdP to be shared across accounts. Creating a grant also provisions a hidden bridge application in the source account.</li>
<li><strong>Share the grant.</strong> Distribute the grant to specific accounts or to your entire organization. Each recipient account is automatically provisioned with a read-only IdP connection that points to the bridge.</li>
</ol>
<p>When a user in a recipient account authenticates, the request is routed through the bridge to the source IdP. The source IdP handles authentication, and the resulting identity claims are passed back to the recipient account's Access policies.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>You must have permission to edit the source IdP in the source account.</li>
<li>You must be a member of a <a href="/fundamentals/organizations/">Cloudflare Organization</a>.</li>
<li>The source account must belong to a Cloudflare Organization.</li>
</ul>
<h2 id="share-an-idp">Share an IdP</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5051.md")
</div></div>
<h2 id="stop-sharing-an-idp">Stop Sharing an IdP</h2>
<p>To stop sharing an IdP, delete the federation grant, as well as the share.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5048.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5054.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<ul>
<li>An account can federate at most one IdP as a source.</li>
<li>A source IdP cannot be deleted while it has a federation grant associated with it. Delete the grant first.</li>
</ul>
