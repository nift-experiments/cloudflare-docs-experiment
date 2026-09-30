<p>In the drand setup phase, you create a collective private and public key pair shared among <em>𝑛</em> participants. This is done through a <code>𝑡-of-𝑛</code> Distributed Key Generation (DKG) process and results in each participant receiving a copy of the collective public key plus a private key share of the collective private key — no individual node knows the collective <strong>private</strong> key. Each private key share can then be used to perform cryptographic threshold computations, such as generating threshold signatures, where at least <code>𝑡</code> contributions produced using the individual private key shares are required to successfully finish the collective operation.</p>
<p>A DKG is performed in a fully distributed manner, avoiding any single points of failure. This is an overview of the different sub-components of the drand DKG implementation.</p>
<h2 id="secret-sharing">Secret Sharing</h2>
<p>Secret sharing is an important technique many advanced threshold cryptography mechanisms rely on.</p>
<p>Secret sharing allows you to split a secret value <code>𝑠</code> into <code>𝑛</code> shares <code>𝑠1,…,𝑠𝑛</code> so that <code>𝑠</code> can only be reconstructed if a threshold of <code>𝑡</code> shares is available.</p>
<h2 id="shamir-s-secret-sharing-sss">Shamir’s Secret Sharing (SSS)</h2>
<p>The SSS scheme is one of the most well-known and widely used secret sharing approaches, and a core component of drand. SSS works over an arbitrary finite field, but a simplistic approach uses the integers modulo <code>𝑝</code>, denoted by <code>ℤ𝑝</code>. Let <code>𝑠∈ℤ𝑝</code> denote the secret to share.</p>
<h3 id="share-distribution">Share Distribution</h3>
<p>To share <code>𝑠</code>, a dealer first creates a polynomial, <code>𝑞(𝑥)=𝑎0+𝑎1𝑥+⋯+𝑎𝑡−1𝑥𝑡−1</code> with <code>𝑎0=𝑠</code> and (random) <code>𝑎𝑖∈ℤ𝑝</code> for <code>𝑖=1,…,𝑡−1</code> and then creates one share 𝑠𝑖 for each participant 𝑖 by evaluating 𝑞(𝑥) at the integer 𝑖 and setting 𝑠𝑖=(𝑖,𝑞(𝑖)).</p>
<h3 id="secret-reconstruction">Secret Reconstruction</h3>
<p>To recover the secret <code>𝑠</code>, collect at least <code>𝑡</code> shares, then uniquely reconstruct <code>𝑞(𝑥)</code> using Lagrange interpolation and obtain <code>𝑠</code> as <code>𝑠=𝑎0=𝑞(0)</code>.</p>
<p>Note that you can use any subset of <code>𝑡-of-𝑛</code> shares to perform Lagrange interpolation and uniquely determine <code>𝑠</code>; however, having a subset of less than <code>𝑡</code> shares does not allow to learn anything about <code>𝑠</code>.</p>
<h2 id="verifiable-secret-sharing">Verifiable Secret Sharing</h2>
<p>SSS scheme assumes that the dealer is honest, but this may not always hold in practice. A Verifiable Secret Sharing (VSS) scheme protects against malicious dealers by enabling participants to verify that their shares are consistent with those dealt to other nodes, ensuring that the shared secret can be correctly reconstructed later.</p>
<p>drand uses Feldman’s VSS scheme, an extension of SSS. Let <code>𝔾</code> denote a cyclic group of prime order <code>𝑝</code> in which computing discrete logarithms is intractable. A <em>cyclic group</em> means there exists a generator, <code>𝑔</code>, so that any element <code>𝑥∈𝔾</code> can be written as <code>𝑥=𝑔𝑎</code> for some <code>𝑎∈{0,…,𝑝−1}</code>.</p>
<h3 id="share-distribution-1">Share Distribution</h3>
<p>In addition to distributing shares of the secret to participants, the dealer also broadcasts commitments to the coefficients of the polynomial <code>𝑞(𝑥)</code> of the form <code>(𝐴0,𝐴1,…,𝐴𝑡−1)=(𝑔𝑠,𝑔𝑎1,…,𝑔𝑎𝑡−1)</code>. These commitments enable individual participants, <code>𝑖</code>, to verify that their share <code>𝑠𝑖=(𝑖,𝑞(𝑖))</code> is consistent with respect to the polynomial <code>𝑞(𝑥)</code> by checking that <code>𝑔𝑞(𝑖)=∏𝑡−1𝑗=0(𝐴𝑗)𝑖𝑗</code> holds.</p>
<h3 id="secret-reconstruction-1">Secret Reconstruction</h3>
<p>The recovery of secret <code>𝑠</code> works the same as regular SSS, except that verified to be valid shares are used.</p>
<h2 id="distributed-key-generation-dkg">Distributed Key Generation (DKG)</h2>
<p>Although VSS schemes protect against a malicious dealer, the dealer still knows the secret. To create a collectively shared secret <code>𝑠</code> so no individual node gets any information about it, participants can use a DKG protocol. drand uses Pedersen’s DKG scheme, which runs <code>𝑛</code> instances of Feldman’s VSS in parallel and on top of additional verification steps.</p>
<h3 id="share-distribution-2">Share Distribution</h3>
<p>Individual participants, <code>𝑖</code>, create a (random) secret, <code>𝑠𝑖∈ℤ𝑝</code>, and share it all participants using VSS, sending a share, <code>𝑠𝑖,𝑗</code> to each <code>𝑗</code> and broadcasts the list of commitments <code>(𝐴𝑖,0,𝐴𝑖,1,…,𝐴𝑖,𝑡−1)</code> to everyone.</p>
<h3 id="share-verification">Share Verification</h3>
<p><code>𝑗</code> verifies the shares received as prescribed by Feldman’s VSS scheme. If <code>𝑗</code> receives an invalid share, <code>𝑠𝑖,𝑗</code>, from <code>𝑖</code>, then <code>𝑗</code> broadcasts a complaint. <code>𝑖</code> must reveal the correct share <code>𝑠𝑖,𝑗</code> or they are considered an invalid dealer.</p>
<h3 id="share-finalization">Share Finalization</h3>
<p>At the end of the protocol, the final share of <code>𝑖</code> is <code>𝑠𝑖=∑𝑗𝑠𝑗,𝑖</code> for all valid participants <code>𝑗</code> , that is, for all <code>𝑗</code>s not excluded during the verification phase.</p>
<p>The collective public key associated with the valid shares can be computed as <code>𝑆=∑𝑗𝐴𝑗,0</code> for all valid <code>𝑗</code>s.</p>
<p><strong>Note:</strong> Even though the secret created using Pedersen’s DKG can be biased, it is safe to use for threshold signing as shown by Rabin et al.</p>
