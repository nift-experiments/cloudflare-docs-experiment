<p>Because of how a waiting room <a href="#background">tracks visitor progress</a>, you need to <a href="#allow-cookies-to-pass-through-iframes">specify certain cookie attributes</a> to properly embed a waiting room in an iFrame.</p>
<h2 id="background">Background</h2>
<p>The <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#samesitesamesite-value"><code>SameSite</code> attribute of a cookie</a> specifies whether that cookie can be shared with other domains that load on the same page (ad banners, iFrames). By default, browsers do not send cookies on cross-site subrequests to prevent attackers from stealing or manipulating information present in your cookies.</p>
<p>However, this behavior can prevent a waiting room from queueing a user properly if that waiting room is embedded in an iFrame. The waiting room depends on the <a href="/waiting-room/reference/waiting-room-cookie/"><code>__cfwaitingroom</code> cookie</a> to track a user in the queue. But, since the browser blocks the cookie from reaching the waiting room by default, an active and queueing waiting room cannot queue the user and will never let them access the application.</p>
<h2 id="available-options">Available options</h2>
<p>To customize how your waiting room responds to cookies, include the <code>cookie_attributes</code> object when you <a href="/api/resources/waiting_rooms/methods/create/">create a waiting room</a> (only available via the API).</p>
<p>Available options include:</p>
<ul>
<li>
<p><code>samesite</code>: Configures the <code>SameSite</code> attribute on the waiting room cookie:</p>
<ul>
<li><strong>auto</strong> (default): Meant to be as flexible as possible, defaulting to <strong>lax</strong> but becoming <strong>none</strong> if you have enabled <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a>.</li>
<li><strong>lax</strong>: Cookies are not sent on typical cross-site subrequests (for example to load images or frames into a third party site), but are sent when a user is navigating to the origin site</li>
<li><strong>strict</strong>: Cookies will only be sent in a first-party context.</li>
<li><strong>none</strong>: Cookies will always be sent.</li>
</ul>
</li>
<li>
<p><code>secure</code>: Configures the <code>Secure</code> attribute on the waiting room cookie, which requires the request to be made over <code>https</code>:</p>
<ul>
<li><strong>auto</strong> (default): Meant to be as flexible as possible, defaulting to <strong>never</strong> but becoming <strong>always</strong> if you have enabled <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a>.</li>
<li><strong>always</strong>: Cookies can only be sent using <code>https</code> requests.</li>
<li><strong>never</strong>: Cookies can be sent using <code>http</code> or <code>https</code> requests.</li>
</ul>
</li>
</ul>
<h2 id="allow-cookies-to-pass-through-iframes">Allow cookies to pass through iFrames</h2>
<p>If you are embedding a waiting room in an iFrame, specify the following values on <code>cookie_attributes</code> object when <a href="/api/resources/waiting_rooms/methods/create/">creating a waiting room</a> (only available via the API):</p>
<ul>
<li><code>samesite</code>: <code>none</code></li>
<li><code>secure</code>: If you have <a href="/ssl/edge-certificates/additional-options/always-use-https/"><strong>Always Use HTTPS</strong></a> enabled, set to <code>auto</code>. If you have it disabled, set to <code>always</code>.</li>
</ul>
<h3 id="example">Example</h3>
<details class="nb-details"><summary>Request</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15756.md")
</div></details>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15757.md")
</div></details>
<h2 id="limitations">Limitations</h2>
<p>Major web browsers have introduced restrictions on third-party cookies, which happen to be the same type of cookies used by waiting rooms within iframes. Waiting Room uses <a href="https://developer.mozilla.org/en-US/docs/Web/Privacy/Privacy_sandbox/Partitioned_cookies">Cookies Having Independent Partitioned State (CHIPS)</a> to work around these restrictions, but there are some drawbacks:</p>
<ul>
<li>A user viewing the waiting room both within an iframe and outside the iframe will be treated as two separate users, with each instance potentially exiting the queue at different times and counting separately in analytics.</li>
<li>For a waiting room to be embedded in an iframe, both the embedded page and the embedding page must be accessed over HTTPS.</li>
<li>CHIPS is not supported on Safari or Safari-derived browsers, like Orion and most iOS browsers, unless they have third-party cookie blocking disabled in their settings. These users will be stuck at the end of the queue, unable to progress until the queue is empty, and may count multiple times in analytics.</li>
</ul>
<p>In general, if there is an issue setting and retrieving the waiting room cookie, you should expect users to be stuck at the end of the queue, and counting as multiple users in analytics.</p>
<p>These limitations may not apply if the embedded page and embedding page share a common domain name. For example, a page at <code>example.com</code> embedding a waiting room at <code>shop.example.com</code> may be considered first party by browsers, and not subject to third-party cookie restrictions.</p>
