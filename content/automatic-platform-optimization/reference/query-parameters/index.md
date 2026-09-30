<p>Query parameters often signal the presence of dynamic content. As a result, if there are query parameters in the URL, APO bypasses the cache and attempts to get a new version of the page from the origin by default. Because query parameters are also often used for marketing attribution, like UTMs, quick loading times are especially important for users.</p>
<p>To add a query parameter to our allowlist, <a href="https://community.cloudflare.com/">create a post in the community</a> for consideration.</p>
<p>APO serves cached content as long as the query parameters in the URL are one of the following:</p>
<ul>
<li><code>ref</code></li>
<li><code>utm_source</code></li>
<li><code>utm_medium</code></li>
<li><code>utm_campaign</code></li>
<li><code>utm_term</code></li>
<li><code>utm_content</code></li>
<li><code>utm_expid</code></li>
<li><code>fbclid</code></li>
<li><code>fb_action_ids</code></li>
<li><code>fb_action_types</code></li>
<li><code>fb_source</code></li>
<li><code>mc_cid</code></li>
<li><code>mc_eid</code></li>
<li><code>gclid</code></li>
<li><code>dclid</code></li>
<li><code>_ga</code></li>
<li><code>campaignid</code></li>
<li><code>adgroupid</code></li>
<li><code>_ke</code></li>
<li><code>cn-reloaded</code></li>
<li><code>age-verified</code></li>
<li><code>ao_noptimize</code></li>
<li><code>usqp</code></li>
<li><code>mkt_tok</code></li>
<li><code>epik</code></li>
<li><code>ck_subscriber_id</code></li>
</ul>
<h2 id="cookies-prefixes-that-always-bypass-cache">Cookies prefixes that always bypass cache</h2>
<ul>
<li><code>wp-</code></li>
<li><code>wordpress</code></li>
<li><code>comment_</code></li>
<li><code>woocommerce_</code></li>
<li><code>xf_</code></li>
<li><code>edd_</code></li>
<li><code>jetpack</code></li>
<li><code>yith_wcwl_session_</code></li>
<li><code>yith_wrvp_</code></li>
<li><code>wpsc_</code></li>
<li><code>ecwid</code></li>
<li><code>ec_</code></li>
<li><code>bookly_</code></li>
<li><code>bookly</code></li>
</ul>
