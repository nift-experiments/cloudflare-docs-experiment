---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/
  description: Manage Access policies in Access.
  full_title: Manage Access policies · Cloudflare One docs
  head_html: <title>Manage Access policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage Access policies in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/index.md"><meta property="og:title" content="Manage Access policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage Access policies in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/#page","headline":"Manage Access policies \u00b7 Cloudflare One docs","description":"Manage Access policies in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/policy-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/policies/policy-management/
  schema: 1
---
<p>Access policies define the users who can log in to your Access applications. You can create, edit, or delete policies at any time and reuse policies across multiple applications.</p>
<h2 id="create-a-policy">Create a policy</h2>
<p>To create a reusable Access policy:</p>
<ol>
<li>In <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Enter a <strong>Policy name</strong>.</li>
<li>Choose an <a href="/cloudflare-one/access-controls/policies/#actions"><strong>Action</strong></a> for the policy.</li>
<li>Choose a <a href="/cloudflare-one/access-controls/access-settings/session-management/"><strong>Session duration</strong></a> for the policy.</li>
<li>Configure as many <a href="/cloudflare-one/access-controls/policies/#rule-types"><strong>Rules</strong></a> as needed.</li>
<li>(Optional) Configure additional settings for users who match this policy:
<ul>
<li><a href="/cloudflare-one/access-controls/policies/isolate-application/">Isolate application</a>.</li>
<li><a href="/cloudflare-one/access-controls/policies/require-purpose-justification/">Purpose justification</a></li>
<li><a href="/cloudflare-one/access-controls/policies/temporary-auth/">Temporary authentication</a></li>
<li><a href="/cloudflare-one/access-controls/policies/mfa-requirements/#independent-mfa">Independent MFA</a></li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>You can now add this policy to an <a href="/cloudflare-one/access-controls/applications/http-apps/">Access application</a>.</p>
<h2 id="edit-a-policy">Edit a policy</h2>
<p>To make changes to an existing Access policy:</p>
<ol>
<li>In <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong>.</li>
<li>Locate the policy you want to update and select <strong>Configure</strong>.</li>
<li>Once you have made the necessary changes, select <strong>Save</strong>.</li>
</ol>
<p>The updated policy is now in effect for all associated Access applications.</p>
<h2 id="delete-a-policy">Delete a policy</h2>
<p>To delete a reusable Access policy:</p>
<ol>
<li>In <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong> and locate the policy you want to delete.</li>
<li>If the policy is used by an application, remove the policy from all associated applications.</li>
<li>Select <strong>Delete</strong>.</li>
<li>A pop-up message will ask you to confirm your decision to delete the policy. Select <strong>Delete</strong>.</li>
</ol>
<h2 id="test-your-policies">Test your policies</h2>
<p>You can test your Access policies against all existing user identities in your Zero Trust organization.  For the policy tester to work, users must have logged into the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> or any other Access application at some point in time.</p>
<p>Cloudflare will use the most recent device that was authenticated with Access to test your policies.</p>
<h3 id="test-a-single-policy">Test a single policy</h3>
<p>The Access policy builder allows you to test your rules before saving any changes.</p>
<p>To test an individual Access policy:</p>
<ol>
<li>In <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong>.</li>
<li>Locate the policy you want to test and select <strong>Configure</strong>.</li>
<li>Go to <strong>Policy tester</strong> and select <strong>Test policies</strong>.</li>
</ol>
<p>The policy tester reports the percentage of active users who are allowed or denied access to an application based on this policy. You can expand the test results to view a list of allowed or blocked users.</p>
<h3 id="test-all-policies-in-an-application">Test all policies in an application</h3>
<p>You can test your Access application policies against your user population before deploying changes to your users. After saving your changes, you can also perform a more detailed policy test for a specific user.</p>
<p>To test if users have access to an application:</p>
<ol>
<li>
<p>In <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Locate the application you want to test and select <strong>Configure</strong>.</p>
</li>
<li>
<p>Go to <strong>Policies</strong> &gt; <strong>Policy tester</strong>.</p>
</li>
<li>
<p>To test all active users in your organization, select <strong>Test policies</strong>.</p>
<pre tabindex="0"><code> The policy tester reports the percentage of users who are allowed or denied access to this application based on all configured policies. You can expand the test results to view a list of allowed or blocked users.&#10;</code></pre>
</li>
<li>
<p>To perform a detailed test on a single user:</p>
<p>a. If you made any changes to your policies, first save the application.</p>
<p>b. Select <strong>testing a single user</strong>.</p>
<p>c. Enter their email address and select <strong>Test policies</strong>.</p>
<p>The single user test results will show:
- Whether the user is allowed or denied access to this application based on all configured policies.
- The user's identity from their most recent Access login attempt.
- Whether the user matches individual Allow, Block, or Bypass policies.</p>
</li>
</ol>
<h2 id="legacy-policies">Legacy policies</h2>
<p>Legacy policies are scoped to a specific application and cannot be added to newly created Access applications.</p>
<h3 id="migrate-to-reusable-policies">Migrate to reusable policies</h3>
<p>To migrate legacy policies to reusable policies:</p>
<ol>
<li><a href="#create-a-policy">Create a reusable policy</a> that will replace the legacy policy.</li>
<li>Go to the Access application associated with the legacy policy.</li>
<li>Add the reusable policy to the application and remove the legacy policy. Removing the legacy policy from the application also deletes it.</li>
<li>Repeat these steps for each legacy policy. If you have duplicate legacy policies, you can replace them with a single reusable policy.</li>
</ol>
<h3 id="convert-a-legacy-policy">Convert a legacy policy</h3>
<p>You can use the API to convert a legacy policy into a reusable policy. To convert a legacy policy, make a <code>PUT</code> request with an empty request body:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/apps/{app_id}/policies/{policy_id}/make_reusable \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>The policy is now removed from the applications endpoint (<code>/access/apps/$APP_ID/policies</code>) and managed using the <a href="/api/resources/zero_trust/subresources/access/subresources/policies/">reusable policies endpoints</a>(<code>/access/policies/$POLICY_ID</code>).</p>
