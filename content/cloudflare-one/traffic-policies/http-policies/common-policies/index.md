<p>The following policies are commonly used to secure HTTP traffic. HTTP policies are evaluated in order from top to bottom, and the first matching policy applies — except for <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect</a> policies, which are always evaluated first.</p>
<p>For a baseline set of recommended policies, refer to <a href="/learning-paths/secure-internet-traffic/build-http-policies/recommended-http-policies/">Secure your Internet traffic and SaaS apps</a>.</p>
<p>Refer to the <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies page</a> for a comprehensive list of other selectors, operators, and actions.</p>
<h2 id="block-sites">Block sites</h2>
<p>Block attempts to reach sites by hostname or URL paths. Different approaches may be required based on how a site is organized.</p>
<h3 id="block-sites-by-hostname">Block sites by hostname</h3>
<p>Block all subdomains that use a host.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6539.md")
</div></div>
<h3 id="block-sites-by-url">Block sites by URL</h3>
<p>Block a section of a site without blocking the entire site. For example, you can block a specific subreddit, such as <code>reddit.com/r/gaming</code>, without blocking <code>reddit.com</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6542.md")
</div></div>
<h2 id="block-content-categories">Block content categories</h2>
<p>Block content categories which go against your organization's acceptable use policy.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6546.md")
</div></div>
<h2 id="block-unauthorized-applications">Block unauthorized applications</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6536.md")
</aside>
<p>To minimize the risk of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6547.md")
</div>, some organizations choose to limit their users' access to certain web-based tools and applications. For example, the following policy blocks known AI tools:
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6551.md")
</div></div>
<h2 id="check-user-identity">Check user identity</h2>
<p>Configure access on a per user or group basis by adding <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based conditions</a> to your policies.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6554.md")
</div></div>
<h2 id="skip-inspection-for-groups-of-applications">Skip inspection for groups of applications</h2>
<p>Certain client applications, such as Zoom or Apple services, rely on certificate pinning. These applications verify they are connecting directly to their own servers and will reject Gateway's TLS inspection certificate. To avoid connection errors, you must add a Do Not Inspect HTTP policy for these applications.</p>
<p>Gateway <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#http-policies">evaluates Do Not Inspect policies first</a>, regardless of their position in the policy list. Cloudflare recommends moving your Do Not Inspect policies to the top of the list to reduce confusion.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6557.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6535.md")
</aside>
<h2 id="check-device-posture">Check device posture</h2>
<p>Require devices to have certain software installed or other configuration attributes. For instructions on setting up a device posture check, refer to <a href="/cloudflare-one/reusable-components/posture-checks/">Enforce device posture</a>.</p>
<h3 id="enforce-a-minimum-os-version">Enforce a minimum OS version</h3>
<p>Perform an <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/">OS version check</a> to ensure users are running at least a minimum version.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6560.md")
</div></div>
<h3 id="check-for-a-specific-file">Check for a specific file</h3>
<p>Perform a <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/file-check/">file check</a> to ensure users have a certain file on their device.</p>
<p>Since the file path will be different for each operating system, you can configure a file check for each system and use the <strong>Or</strong> logical operator to only require one of the checks to pass.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6563.md")
</div></div>
<h2 id="enforce-session-duration">Enforce session duration</h2>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Require users to re-authenticate</a> after a certain amount of time has elapsed.</p>
<h2 id="isolate-high-risk-sites-in-remote-browser">Isolate high risk sites in remote browser</h2>
<p>If you are using the <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation add-on</a>, refer to our list of <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/#common-policies">common Isolate policies</a>.</p>
<h2 id="bypass-inspection-for-self-signed-certificates">Bypass inspection for self-signed certificates</h2>
<p>When accessing origin servers with certificates not signed by a public certificate authority, you must bypass TLS decryption.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6566.md")
</div></div>
<h2 id="block-file-types">Block file types</h2>
<p>Block the upload or download of files based on their type.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6569.md")
</div></div>
<p>For more information on supported file types, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types">Download and Upload File Types</a>.</p>
<h2 id="isolate-or-block-shadow-it-applications">Isolate or block shadow IT applications</h2>
<p>Isolate shadow IT applications discovered by the <a href="/cloudflare-one/team-and-resources/app-library/">Application Library</a> that have not been reviewed yet or are currently under review, and block applications that are not approved by your organization.</p>
<p>For more information on reviewing shadow IT applications, refer to <a href="/cloudflare-one/team-and-resources/app-library/#review-applications">Review applications</a>.</p>
<h3 id="1-isolate-unreviewed-or-in-review-applications"><ol>
<li>Isolate unreviewed or in review applications</li>
</ol></h3>
<p>Isolate applications if their approval status is <em>Unreviewed</em> or <em>In review</em>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6572.md")
</div></div>
<h3 id="2-block-unapproved-applications"><ol start="2">
<li>Block unapproved applications</li>
</ol></h3>
<p>Block applications if their approval status is <em>Unapproved</em>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6575.md")
</div></div>
<h2 id="block-google-services">Block Google services</h2>
<p>To enable Gateway inspection for Google Drive traffic, you must <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/#google-drive">add a Cloudflare certificate to Google Drive</a>.</p>
<h3 id="block-google-drive-downloads">Block Google Drive downloads</h3>
<p>Block file downloads from Google Drive.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6578.md")
</div></div>
<h3 id="block-google-drive-uploads">Block Google Drive uploads</h3>
<p>Block file uploads from Google Drive.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6581.md")
</div></div>
<h3 id="block-gmail-downloads">Block Gmail downloads</h3>
<p>Block file downloads from Gmail.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6584.md")
</div></div>
<h3 id="block-google-translate-proxy">Block Google Translate proxy</h3>
<p>Block use of Google Translate to translate entire webpages.</p>
<p>When translating a website, Google Translate proxies webpages with the <code>translate.goog</code> domain. Your users may be able to use this service to bypass other Gateway policies. If you block <code>translate.goog</code>, users will still be able to access other Google Translate features.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6587.md")
</div></div>
<h2 id="filter-websocket-traffic">Filter WebSocket traffic</h2>
<p>Gateway does not inspect or log <a href="https://datatracker.ietf.org/doc/html/rfc6455">WebSocket</a> traffic. Instead, Gateway will only log the HTTP details used to make the WebSocket connection, as well as <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">network session information</a>. To filter your WebSocket traffic, create a policy with the <code>101</code> HTTP response code.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6590.md")
</div></div>
