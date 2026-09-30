<p>drand is an efficient randomness beacon daemon that utilizes pairing-based cryptography, <code>𝑡-of-𝑛</code> distributed key generation, and threshold BLS signatures to generate publicly-verifiable, unbiasable, unpredictable, distributed randomness.</p>
<p>This is an overview of the cryptographic building blocks drand uses to generate publicly-verifiable, unbiasable, and unpredictable randomness in a distributed manner.</p>
<p>The drand beacon has two phases: a setup phase and a beacon phase. Generally, we assume that there are <em>n</em> participants, out of which at most <em>f&lt;n</em> are malicious. drand relies heavily on threshold cryptography primitives, where (at minimum) a threshold of <em>t-f+1</em> nodes work together to successfully execute cryptographic operations.</p>
<p>Threshold cryptography has many applications as it avoids single points of failure. One application is cryptocurrency multi-sig wallets, where <em>t-of-n</em> participants are required to sign a transaction using a threshold signature scheme.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/11563.md")
</aside>
