<p>Mutual TLS (mTLS) authentication uses client certificates to ensure traffic between client and server is bidirectionally secure and trusted. mTLS also allows requests that do not authenticate via an identity provider — such as Internet-of-things (IoT) devices — to demonstrate they can reach a given resource.</p>
<p><img src="/assets/upstream/images/api-shield/api-shield-call-sequence.png" alt="mTLS sequence diagram" /></p>
<p>Support includes <a href="https://grpc.io/docs/what-is-grpc/introduction/">gRPC</a>-based APIs, which use binary formats such as protocol buffers rather than JSON.</p>
<h2 id="creating-a-mtls-rule">Creating a mTLS rule</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9626.md")
</div>
<p>Once you have deployed your mTLS rule, any requests without a <a href="/ssl/client-certificates/">valid client certificate</a> will be blocked.</p>
