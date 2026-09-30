<p>If you are using Media Transformations to transform your video and you experience a failure, the response body contains an error message explaining the reason, as well as the <code>Cf-Resized</code> header containing <code>err=code</code>:</p>
<ul>
<li>9401 — The required options are missing or are invalid. Refer to <a href="/stream/transform-videos/#options">Options</a> for supported arguments.</li>
<li>9402 — The video was too large or the origin server did not respond as expected. Refer to <a href="/stream/transform-videos/#source-video-requirements">source video requirements</a> for more information.</li>
<li>9404 — The video does not exist on the origin server or the URL used to transform the video is wrong. Verify the video exists and check the URL.</li>
<li>9406 &amp; 9419 — The video URL is a non-HTTPS URL or the URL has spaces or unescaped Unicode. Check your URL and try again.</li>
<li>9407 — A lookup error occurred with the origin server's domain name. Check your DNS settings and try again.</li>
<li>9408 — The origin server returned an HTTP 4xx status code and may be denying access to the video. Confirm your video settings and try again.</li>
<li>9412 — The origin server returned a non-video, for example, an HTML page. This usually happens when an invalid URL is specified or server-side software has printed an error or presented a login page.</li>
<li>9504 — The origin server could not be contacted because the origin server may be down or overloaded. Try again later.</li>
<li>9509 — The origin server returned an HTTP 5xx status code. This is most likely a problem with the origin server-side software, not the transformation.</li>
<li>9517 &amp; 9523 — Internal errors. Contact support if you encounter these errors.</li>
</ul>
<hr />
