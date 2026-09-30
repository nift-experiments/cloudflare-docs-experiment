<h2 id="2026-07-22">2026-07-22</h2><ul>
<li>Turnstile may now make requests to <code>hagen.challenges.cloudflare.com</code> or <code>brunhild.challenges.cloudflare.com</code> as part of browser verification. Add both hostnames to your network allowlist so Turnstile can access them. For more information, refer to <a href="/cloudflare-challenges/troubleshooting/challenge-solve-issues/#failed-subdomain-network-requests-during-turnstile-challenges">Failed subdomain network requests during Turnstile challenges</a>.</li>
</ul><h2 id="2024-08-12">2024-08-12</h2><ul>
<li>Added <a href="/turnstile/get-started/client-side-rendering/#widget-size"><code>[flexible]</code></a> width widget size.</li>
<li>Added new dimensions for Turnstile's compact size.</li>
<li>Added a Feedback Report toggle on the widget's configuration.</li>
</ul><h2 id="2024-04-10">2024-04-10</h2><ul>
<li>Added <a href="/turnstile/get-started/client-side-rendering/#refresh-a-timed-out-widget"><code>[refresh-timeout]</code></a> and document new automatic interactive timeout-refresh.</li>
</ul><h2 id="2024-03-25">2024-03-25</h2><ul>
<li>Added more <a href="/turnstile/reference/supported-languages">supported languages</a>.</li>
</ul><h2 id="2023-12-18">2023-12-18</h2><ul>
<li>Added <a href="/turnstile/concepts/pre-clearance-support/">Pre-Clearance mode</a>.</li>
</ul><h2 id="2023-08-24">2023-08-24</h2><ul>
<li>Added <a href="/turnstile/troubleshooting/client-side-errors/">Client-side errors</a>.</li>
</ul><h2 id="2023-07-31">2023-07-31</h2><ul>
<li>Added <a href="/turnstile/get-started/client-side-rendering/#access-a-widgets-state"><code>[turnstile.isExpired]</code></a>.</li>
<li>Added <code>uk</code> language.</li>
</ul><h2 id="2023-05-25">2023-05-25</h2><ul>
<li>Added idempotency support for <code>POST /siteverify</code> requests via the <code>idempotency_key</code> parameter.</li>
</ul><h2 id="2023-04-17">2023-04-17</h2><ul>
<li>Added references to Turnstile Public API.</li>
<li>Added references for <a href="/turnstile/get-started/client-side-rendering/#explicitly-render-the-turnstile-widget"><code>[after-interactive-callback]</code></a>, <a href="/turnstile/get-started/client-side-rendering/#explicitly-render-the-turnstile-widget"><code>[before-interactive-callback]</code></a>, and <a href="/turnstile/get-started/client-side-rendering/#explicitly-render-the-turnstile-widget"><code>[unsupported-callback]</code></a>.</li>
</ul><h2 id="2023-03-06">2023-03-06</h2><ul>
<li>Added <a href="/turnstile/get-started/client-side-rendering/#explicitly-render-the-turnstile-widget"><code>[execution]</code></a> and <a href="/turnstile/get-started/client-side-rendering/#explicitly-render-the-turnstile-widget"><code>[appearance]</code></a>.</li>
</ul><h2 id="2023-02-15">2023-02-15</h2><ul>
<li>Added the <a href="/turnstile/get-started/client-side-rendering/#explicitly-render-the-turnstile-widget"><code>[turnstile.ready]</code></a> callback.</li>
</ul><h2 id="2023-02-01">2023-02-01</h2><ul>
<li>Added the <a href="/turnstile/get-started/client-side-rendering/#configurations"><code>[data-]language</code></a> parameter.</li>
</ul><h2 id="2022-12-12">2022-12-12</h2><ul>
<li><a href="/turnstile/get-started/server-side-validation/"><code>POST /siteverify</code></a> supports JSON requests now.</li>
</ul><h2 id="2022-11-11">2022-11-11</h2><ul>
<li>Added <a href="/turnstile/get-started/client-side-rendering/#configurations"><code>retry</code> and <code>retry-interval</code></a> for controlling retry behavior.</li>
</ul><h2 id="2022-10-28">2022-10-28</h2><ul>
<li>Renamed the <code>[data-]expired-callback</code> callback to <a href="/turnstile/get-started/client-side-rendering/#configurations"><code>[data-]timeout-callback</code></a> (called when the challenge times out).</li>
<li>Added the <a href="/turnstile/get-started/client-side-rendering/#configurations"><code>[data-]expired-callback</code></a> callback (called when the token expires).</li>
</ul><h2 id="2022-10-24">2022-10-24</h2><ul>
<li>Added <a href="/turnstile/get-started/client-side-rendering/#configurations"><code>response-field</code> and <code>response-field-name</code></a> for controlling the input element created by Turnstile.</li>
<li>Added option for changing the <a href="/turnstile/get-started/client-side-rendering/#widget-size">size of the Turnstile widget</a>.</li>
</ul><h2 id="2022-10-13">2022-10-13</h2><ul>
<li>Added validation for action: <code>/^[a-z0-9_-]{0,32}$/i</code></li>
<li>Added validation for cData: <code>/^[a-z0-9_-]{0,255}$/i</code></li>
</ul><h2 id="2022-10-11">2022-10-11</h2><ul>
<li>Added <a href="/turnstile/get-started/client-side-rendering/#remove-a-widget"><code>turnstile.remove</code></a></li>
</ul>
