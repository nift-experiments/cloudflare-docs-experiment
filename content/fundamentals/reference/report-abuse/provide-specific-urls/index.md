<p>If you are <a href="https://abuse.cloudflare.com">submitting an abuse report</a> to Cloudflare because our IP address appears in the WHOIS and DNS records for a website, it is very likely that the website is one of millions of websites that use our pass-through security and content distribution network (CDN) services. Because assets on the same website may be hosted by different providers, it is important that you submit the URL for that specific asset to enable appropriate action. This guide will teach you how to identify URLs for specific video or images on a webpage.</p>
<h2 id="get-the-url-for-specific-content">Get the URL for specific content</h2>
<p>To get the URL for a specific piece of content on a webpage:</p>
<ol>
<li>
<p>Open your web browser (Google Chrome, Safari, Firefox, Edge).</p>
</li>
<li>
<p>Go to the web page you want to report.</p>
</li>
<li>
<p>Right click on the content you wish to report (often a video or image).</p>
</li>
<li>
<p>Select <strong>Inspect Element</strong>.</p>
</li>
<li>
<p>In the <strong>DevTools</strong> panel, look for the <strong>src</strong> attribute in the selected the image, video, or iFrame.
<img src="/assets/upstream/images/fundamentals/get-started/identify-url.png" alt="Look for the URL in the src attribute of the video or image" /></p>
</li>
<li>
<p>Copy the URL.</p>
</li>
</ol>
<p>Providing the most specific and helpful URL enables Cloudflare to correctly identify any services it may be providing with respect to that content.</p>
<h2 id="submitting-the-abuse-report">Submitting the abuse report</h2>
<p>Once you have identified the URL for the specific asset, you can <a href="https://abuse.cloudflare.com">submit an abuse report</a> through Cloudflare's online abuse reporting process.</p>
<p>You can learn more about the process, and what you can expect from Cloudflare in response to such abuse reports, from <a href="https://www.cloudflare.com/trust-hub/reporting-abuse/">our abuse policy</a>.</p>
