<p>Cloudflare's Keyless SSL technology was designed to scale to accommodate any sized workload using vertical and horizontal scaling, and pre-computation techniques wherever possible, such as ECDSA. The goals of the architectural design of the key server are to minimize latency while maximizing signing operations per second.</p>
<p>Each key server uses a worker pool model, with incoming client connections handled by its own pair of reader/writer goroutines and cryptographic work done in separate worker goroutines pulled from a global pool.</p>
<p>Where needed, multiple key servers can be deployed and balanced between using your preferred ingress load balancing configuration. For full high availability, make sure to deploy sufficient key servers to handle twice the expected workload.</p>
<hr />
<h2 id="key-type">Key type</h2>
<p>Key servers support both ECDSA and RSA keys, though signatures for RSA are an <a href="https://blog.cloudflare.com/ecdsa-the-digital-signature-algorithm-of-a-better-internet/">order of magnitude more expensive</a> to compute and thus consider type of keys used when planning the number of key servers in your deployment.</p>
<p>ECDSA signing can be broken down into two steps. Since the first step — generating random values (to be used later with the private key and message to be signed) — represents the majority of the computational cost, we pre-generate these random values to significantly reduce latency. ECDSA signing requests are computationally isolated from RSA signing requests using separate worker pools to keep them as fast as possible.</p>
<p>Additional details can be found in the <a href="https://github.com/cloudflare/gokeyless#readme">gokeyless server readme file</a> file.</p>
<hr />
<h2 id="benchmarks">Benchmarks</h2>
<p>We conducted benchmarks using <a href="https://github.com/cloudflare/gokeyless/tree/master/cmd/bench">Cloudflare's gokeyless bench tool</a> on a then current-generation, compute-optimized EC2 instance (<a href="https://aws.amazon.com/ec2/instance-types/c5/">c5.xlarge</a>). This particular instance has 4 vCPUs powered by 3.0 GHz Intel Xeon processors:</p>
<pre><code class="language-txt">c5$ cat /proc/cpuinfo|grep &quot;model name&quot;&#10;model name	: Intel(R) Xeon(R) Platinum 8124M CPU @ 3.00GHz&#10;model name	: Intel(R) Xeon(R) Platinum 8124M CPU @ 3.00GHz&#10;model name	: Intel(R) Xeon(R) Platinum 8124M CPU @ 3.00GHz&#10;model name	: Intel(R) Xeon(R) Platinum 8124M CPU @ 3.00GHz&#10;</code></pre>
<p>By default, bench runs with one worker goroutine per core (4) and a maximum number of operating system threads equal to the total number of cores (in this case, <code>GOMAXPROCS=4</code>). As expected and explained above, ECDSA signature performance far exceeds that of RSA. The <a href="#results">results show</a> that each core of this c5.xl machine can perform over 10,000 ECDSA signing operations/second and approximately 200 RSA signing operations/second.</p>
<p>When planning your deployment, determine the maximum number of new TLS connections per second you expect to terminate using a given key server and scale accordingly. For full high availability, each data center running keyless should be able to terminate the full workload that you anticipate.</p>
<h3 id="results">Results</h3>
<h4 id="ecdsa">ECDSA</h4>
<pre><code class="language-txt">c5$ bench -ski $ECDSA_SKI -op ECDSA-SHA256 -bandwidth -duration 60s&#10;Total operations completed: 2661570&#10;Average operation duration: 22.543µs&#10;</code></pre>
<h4 id="rsa">RSA</h4>
<pre><code class="language-txt">c5$ bench -ski $RSA_SKI -op RSA-SHA256 -bandwidth -duration 60s&#10;Total operations completed: 46560&#10;Average operation duration: 1.288659ms.&#10;</code></pre>
