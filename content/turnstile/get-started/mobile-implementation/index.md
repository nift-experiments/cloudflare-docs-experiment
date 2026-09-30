<p>Turnstile requires a browser environment because it runs JavaScript challenges in the visitor's browser. On mobile devices, Turnstile works in mobile browsers without additional configuration.</p>
<p>For native mobile applications, Turnstile does not run natively. Instead, you use a WebView — a browser component embedded inside your native app — to load a webpage that contains the Turnstile widget.</p>
<hr />
<h2 id="webview-integration">WebView integration</h2>
<p>A WebView embeds a browser engine within your native application, enabling you to show web pages, forms, and JavaScript-powered content like Turnstile widgets.</p>
<h3 id="requirements">Requirements</h3>
<p>For Turnstile to function properly in WebView, the following requirements must be met.</p>
<h4 id="javascript-support">JavaScript support</h4>
<ul>
<li>JavaScript execution must be enabled.</li>
<li>DOM storage API must be available.</li>
<li>Standard web APIs must be accessible.</li>
</ul>
<h4 id="network-access">Network access</h4>
<ul>
<li>Access to <code>challenges.cloudflare.com</code></li>
<li>Support for both HTTP and HTTPS connections.</li>
<li>Allow connections to <code>about:blank</code> and <code>about:srcdoc</code></li>
</ul>
<h4 id="environment-consistency">Environment consistency</h4>
<ul>
<li>Consistent User Agent throughout the session</li>
<li>Stable device and browser characteristics</li>
<li>No modification to core browser behavior</li>
</ul>
<h3 id="platform-specific-implementation">Platform-specific implementation</h3>
<h4 id="android-webview">Android WebView</h4>
<pre><code class="language-java">WebView webView = findViewById(R.id.webview);&#10;WebSettings webSettings = webView.getSettings();&#10;&#10;// Required: Enable JavaScript&#10;webSettings.setJavaScriptEnabled(true);&#10;&#10;// Required: Enable DOM storage&#10;webSettings.setDomStorageEnabled(true);&#10;&#10;// Recommended: Enable other web features&#10;webSettings.setLoadWithOverviewMode(true);&#10;webSettings.setUseWideViewPort(true);&#10;webSettings.setAllowFileAccess(true);&#10;webSettings.setAllowContentAccess(true);&#10;&#10;// Load your web content with Turnstile&#10;webView.loadUrl(&quot;https://yoursite.com/protected-form&quot;);&#10;</code></pre>
<h4 id="ios-wkwebview-swift">iOS WKWebView (Swift)</h4>
<pre><code class="language-swift">import WebKit&#10;&#10;class ViewController: UIViewController {&#10;    @IBOutlet weak var webView: WKWebView!&#10;&#10;    override func viewDidLoad() {&#10;        super.viewDidLoad()&#10;&#10;        // Configure WebView&#10;        let configuration = WKWebViewConfiguration()&#10;        configuration.preferences.javaScriptEnabled = true&#10;&#10;        // Load your web content with Turnstile&#10;        if let url = URL(string: &quot;https://yoursite.com/protected-form&quot;) {&#10;            webView.load(URLRequest(url: url))&#10;        }&#10;    }&#10;}&#10;</code></pre>
<h4 id="react-native-webview">React Native WebView</h4>
<pre><code class="language-js">import { WebView } from &quot;react-native-webview&quot;;&#10;&#10;export default function App() {&#10;	return (&#10;		&lt;WebView&#10;			source={{ uri: &quot;https://yoursite.com/protected-form&quot; }}&#10;			javaScriptEnabled={true}&#10;			domStorageEnabled={true}&#10;			allowsInlineMediaPlayback={true}&#10;			mediaPlaybackRequiresUserAction={false}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
<h4 id="flutter-webview">Flutter WebView</h4>
<pre><code class="language-dart">import &#x27;package:flutter_inappwebview/flutter_inappwebview.dart&#x27;;&#10;&#10;class WebViewScreen extends StatelessWidget {&#10;  @override&#10;  Widget build(BuildContext context) {&#10;    return InAppWebView(&#10;      initialUrlRequest: URLRequest(&#10;        url: Uri.parse(&#x27;https://yoursite.com/protected-form&#x27;)&#10;      ),&#10;      initialOptions: InAppWebViewGroupOptions(&#10;        crossPlatform: InAppWebViewOptions(&#10;          javaScriptEnabled: true,&#10;          useShouldOverrideUrlLoading: false,&#10;        ),&#10;        android: AndroidInAppWebViewOptions(&#10;          domStorageEnabled: true,&#10;        ),&#10;        ios: IOSInAppWebViewOptions(&#10;          allowsInlineMediaPlayback: true,&#10;        ),&#10;      ),&#10;    );&#10;  }&#10;}&#10;</code></pre>
<hr />
<h2 id="common-implementation-issues">Common implementation issues</h2>
<h3 id="user-agent-consistency">User Agent consistency</h3>
<p>Changing the User Agent during a session causes Turnstile challenges to fail because the system relies on consistent browser characteristics to validate the visitor's authenticity. When the User Agent changes mid-session, Turnstile treats this as a potential security risk and rejects the challenge.</p>
<pre><code class="language-java">// Android - Set consistent User Agent&#10;webSettings.setUserAgentString(webSettings.getUserAgentString());&#10;</code></pre>
<pre><code class="language-swift">// iOS - Maintain default User Agent&#10;webView.customUserAgent = webView.value(forKey: &quot;userAgent&quot;) as? String&#10;</code></pre>
<h3 id="content-security-policy-csp">Content Security Policy (CSP)</h3>
<p>Strict <a href="/turnstile/reference/content-security-policy/">Content Security Policy</a> settings can prevent Turnstile from loading the necessary scripts and making required network connections. This happens when CSP headers or meta tags block access to the domains and resources that Turnstile needs to function properly.</p>
<pre><code class="language-html">&lt;meta&#10;	http-equiv=&quot;Content-Security-Policy&quot;&#10;	content=&quot;&#10;  default-src &#x27;self&#x27;; &#10;  script-src &#x27;self&#x27; challenges.cloudflare.com &#x27;unsafe-inline&#x27;; &#10;  connect-src &#x27;self&#x27; challenges.cloudflare.com;&#10;  frame-src &#x27;self&#x27; challenges.cloudflare.com;&#10;&quot;&#10;/&gt;&#10;</code></pre>
<h3 id="domain-configuration">Domain configuration</h3>
<p>WebView security restrictions can prevent access to the domains that Turnstile requires for proper operation. Some WebViews are configured to only allow specific domains or block certain types of connections, which can interfere with Turnstile's ability to load challenges and communicate with Cloudflare's servers.</p>
<p>To resolve this, configure your WebView's allowed origins to include all domains that Turnstile needs:</p>
<ul>
<li><code>challenges.cloudflare.com</code></li>
<li><code>about:blank</code></li>
<li><code>about:srcdoc</code></li>
<li>Your own domain(s)</li>
</ul>
<p>The exact configuration method varies by platform, but the principle is to explicitly allow network access for these domains.</p>
<h3 id="cookie-and-storage-issues">Cookie and storage issues</h3>
<p>Cookies and local storage not persisting between sessions can cause Turnstile to fail because it relies on these mechanisms to maintain state and track visitor behavior. This commonly occurs when WebView storage settings are too restrictive or when the app clears storage between sessions. Ensure that your WebView is configured to properly handle cookies and local storage.</p>
<pre><code class="language-java">// Android - Enable cookies&#10;CookieManager.getInstance().setAcceptCookie(true);&#10;CookieManager.getInstance().setAcceptThirdPartyCookies(webView, true);&#10;</code></pre>
<pre><code class="language-swift">// iOS - Configure cookie storage&#10;webView.configuration.websiteDataStore = WKWebsiteDataStore.default()&#10;</code></pre>
