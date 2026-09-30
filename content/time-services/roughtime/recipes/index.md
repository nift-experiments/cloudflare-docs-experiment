<p>There are various ways you can use Roughtime to keep your clock in sync. These recipes use <a href="https://github.com/cloudflare/roughtime">Cloudflare's Go package</a>, which is based on Google's <a href="https://roughtime.googlesource.com/roughtime/+/master/go/client/">Go
client</a>.</p>
<p>The protocol is also implemented in <a href="https://roughtime.googlesource.com/roughtime/+/master">C++</a>, <a href="https://github.com/int08h/roughenough">Rust</a>, and
<a href="https://github.com/int08h/nearenough">Java</a>.</p>
<h2 id="client-configuration">Client configuration</h2>
<p>The client configuration consists of a list of named Roughtime servers
formatted as a JSON object. For example:</p>
<pre><code class="language-json">{&#10;  &quot;servers&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;Cloudflare-Roughtime-2&quot;,&#10;      &quot;publicKeyType&quot;: &quot;ed25519&quot;,&#10;      &quot;publicKey&quot;: &quot;0GD7c3yP8xEc4Zl2zeuN2SlLvDVVocjsPSL8/Rl/7zg=&quot;,&#10;      &quot;addresses&quot;: [&#10;        {&#10;          &quot;protocol&quot;: &quot;udp&quot;,&#10;          &quot;address&quot;: &quot;roughtime.cloudflare.com:2003&quot;&#10;        }&#10;      ]&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>It includes each server's <em>root public key</em>. When the server starts, it
generates an <em>online</em> public/secret key pair. The root secret key is used to create a <em>delegation</em> for the online public key and the online secret key is used to sign the response.</p>
<p>The delegation serves the same function as a traditional <a href="https://en.wikipedia.org/wiki/X.509">X.509 certificate</a> on the web. The client first uses the root public key to verify the delegation, then uses the online public key to verify the response.</p>
<p>Because the response is <em>auditable</em>, the protocol makes each client accountable to provide accurate time.</p>
<p>The configuration also encodes the type of signature algorithm used by the
server (currently only <a href="https://en.wikipedia.org/wiki/EdDSA">Ed25519</a> is supported). Lastly, the configuration contains a list of addresses where the service can be reached and which transport protocol to use to reach them (currently only UDP is supported).</p>
<h2 id="tls">TLS</h2>
<p>A good starting example would be to sync a TLS client or server using a single Roughtime server. That would involve computing the time difference between our clock and the Roughtime sever's.</p>
<p>The first step is to load the configuration file (be sure to</p>
<pre><code class="language-go">servers, skipped, err := roughtime.LoadConfig(&quot;roughtime.config&quot;)&#10;</code></pre>
<p>In this example, the variable <code>servers</code> is the list of valid server configurations parsed from the input file. The variable <code>skipped</code> indicates the number of servers that were skipped, for example, if the signature algorithm or transport protocol was not supported.</p>
<p>Next, we would get the system time and query the first server in the list:</p>
<pre><code class="language-go">t0 := time.Now()&#10;rt, err := roughtime.Get(&amp;servers[0], attempts, timeout, nil)&#10;</code></pre>
<p>This sends a request to the server and verifies the response. The variable <code>rt</code> is of type <code>*roughtime.Roughtime</code> and represents the result of the query. The inputs are:</p>
<ol>
<li>The server's configuration.</li>
<li>The number of attempts to dial the server.</li>
<li>The time to wait for each dial attempt.</li>
<li>An optional <code>*roughtime.Roughtime</code>, the result of a prior query.</li>
</ol>
<p>If the last parameter is provided, then it's used generate the nonce for the
request (more on this later).</p>
<p>The <code>crypto/tls</code> package allows the user to
<a href="https://golang.org/pkg/crypto/tls/#Config">specify a callback</a> for the current time to use when validating certificates, session tickets, etc. You can compute this callback as follows:</p>
<pre><code class="language-go">t1, radius := rt.Now()&#10;delta := t1.Sub(t0.Now())&#10;now := func() time.Time {&#10;  return time.Now().Add(delta)&#10;}&#10;</code></pre>
<p>The variable <code>t1</code> is the time reported by the server and <code>radius</code> is the server's uncertainty radius.</p>
<p>For a full working example, check out our
<a href="https://github.com/cloudflare/roughtime/blob/master/recipes/tls.go">GitHub</a>.</p>
<h2 id="desktop-alerts">Desktop alerts</h2>
<p>A more general way to use Roughtime is to create desktop alerts that warn you when your clock is skewed.</p>
<p>On Ubuntu GNU/Linux, you can do something like this:</p>
<pre><code class="language-go">skew := time.Duration(math.Abs(float64(delta)))&#10;if skew &gt; 10*time.Second {&#10;  summary := &quot;Check your clock!&quot;&#10;  body := fmt.Sprintf(&quot;%s says it&#x27;s off by %v.&quot;, servers[0].Name, skew)&#10;  cmd := exec.Command(&quot;notify-send&quot;, &quot;-i&quot;, &quot;clock&quot;, summary, body)&#10;  if err := cmd.Run(); err != nil {&#10;    // error handling ...&#10;  }&#10;}&#10;</code></pre>
<p>For a full working example, check out our <a href="https://github.com/cloudflare/roughtime/tree/master/recipes/alerter.go">GitHub</a> (tested on Ubuntu 18.04). You would run this program as a cron job to periodically check that your clock is in sync.</p>
<h2 id="using-multiple-sources">Using multiple sources</h2>
<p>Using multiple sources for Roughtime is easy (and highly recommended):</p>
<pre><code class="language-go">t0 := time.Now()&#10;res := roughtime.Do(servers, attempts, timeout, nil)&#10;</code></pre>
<p>The first parameter is a sequence of servers and the remaining parameters are the same as in <code>roughtime.Get()</code>. This queries each server in the sequence <code>servers</code> in order. The output <code>res</code> is a slice the same length as <code>servers</code>.</p>
<p>Each element represents the result of the query to the server. If the query was successful, then the result contains the server's time. If unsuccessful, then the result contains the error that occurred. To compute the median difference between your clock and the valid responses:</p>
<pre><code class="language-go">thresh := 10 * time.Second&#10;delta, err := roughtime.MedianDeltaWithRadiusThresh(res, t0, thresh)&#10;</code></pre>
<p>This rejects responses whose uncertainty radii exceed 10 seconds. An error will be returned if there were no valid responses.</p>
<h3 id="auditing-your-sources">Auditing Your Sources</h3>
<p>Function <code>roughtime.Do()</code> chains together valid responses, generating each nonce using the server's response in the last successful query. As we discuss in more detail in the <a href="https://blog.cloudflare.com/roughtime/">blog</a>, linking queries together in this manner results in cryptographic proof that the queries were made in order. To verify that the results have this property, you can do the following:</p>
<pre><code class="language-go">chain := roughtime.NewChain(results)&#10;ok, err := chain.Verify(nil)&#10;if err != nil || !ok {&#10;  // error handling ...&#10;}&#10;</code></pre>
<p>The variable <code>chain</code> is a structure that contains the first successful query in <code>results</code>. It has a field, <code>chain.Next</code>, that points to the next successful query. The input parameter to <code>Verify()</code> allows you to use a previous result as a starting point for verifying the chain. For example, if <code>chain.Verify(nil)</code> is valid, then <code>chain.Next.Verify(chain.Roughtime)</code> will be valid, too.</p>
<h3 id="being-verbose">Being Verbose</h3>
<p>It is possible to have <code>roughtime.Do()</code> output useful information as it executes its queries. To do so, invoke <code>roughtime.SetLogger()</code> to set a logger. For example:</p>
<pre><code class="language-go">roughtime.SetLogger(log.New(os.Stdout, &quot;&quot;, 0))&#10;</code></pre>
