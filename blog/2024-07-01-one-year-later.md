# One Year Later on Juno

Hello! I'm Dimi 🦙. For those who don't know me, I helped found Juno, contributing to its launch phase with my protocols and engineering abilities. This note is a sequel to [my previous one](https://dimi.sh/blog/2023-06-23-why-juno.html), released now more than one year ago.

## What happened

After my article, Juno went through a massive reorganization. A group of volunteers from the community proposed [The Charter](https://www.mintscan.io/juno/proposals/319), which went live shortly after.

To summarize, The Charter is a combination of various sub-DAOs of the Juno Network that aims to enhance transparency and manage the chain in all its aspects, including operations, communications, and development.

It took several months to become fully operational, with public elections, lots of people involved, and many community discussions. It became fully operative only around January 2024.

In the past 6 months of The Charter, Juno reached a level of decentralization and transparency like never before, accomplished the clearance of previous agreements, and worked to define a budget for the chain's growth.

However, all this decentralization and transparency quickly highlighted the inefficiencies of The Charter itself. It took weeks to make even the simplest decision, with a long bureaucratic and tiring process for everyone.

Due to this slowness, The Charter wasn't able to deliver enough to the Juno community, essentially focusing only on organizing The Charter itself rather than driving the network in a new direction.

The Charter is now going to be disbanded with [this proposal](https://www.mintscan.io/juno/proposals/350). With my personal stake and my validator company, I voted NO because I thought the best path forward would have been to fix The Charter's inefficiencies and keep working with the great people who contributed so much to it. Unfortunately, the proposal passed, so now we need to think about something new.

## Today

Most of The Charter department members took proposal 350 literally and immediately removed themselves from the various DAOs, effectively locking treasury and tokens in smart contracts that are now impossible to access without a software upgrade or admin on-chain proposals. Additionally, the proposal was poorly worded, and I can't see a way to continue the delegation program without putting the 10M JUNO tokens at risk in the hands of a few people.

As of today, no one is effectively managing the chain. There is no roadmap. There is no objective. It's chaos.

This may sound tragic, but it can also be a huge opportunity to restart and try again with something new, learning from past mistakes.

And no worries - I'll keep working on Juno Core as I always did since genesis. Yes, I was here when Reece was here, I was here when The Frey was here, I was here when Notional was here, and so on. So we are covered, at least with basic upgrades and security patches.

## Next

This is the most fun part because we can do something to quickly get things up and running again, this time hopefully with a solid solution that can last a long time.

I think the next steps should be:

1. Define a new, more efficient organizational structure.
2. Revisit tokenomics, locked balances, vesting, inflation, and governance.
3. Clean up Juno Core code and write the necessary upgrades.
4. Build dApps internally.

Let's tackle each of these one by one.

### New structure

What was really missing in The Charter was someone giving direction to it, someone taking responsibility for decisions. The whole Charter idea was based on the fact that departments would check and balance each other, but in the real world, that doesn't happen. Human collaboration requires leadership to avoid getting stuck.

A structure that may be efficient is the following:

![Juno Structure](https://dimi.sh/img/juno-structure.png)


1. **Juno Leader**: This should be elected by the community. Anyone should be able to apply as a leader, and every mandate should be 6-12 months long. To apply, a leader has to provide the following: Previous experience with Juno, conflict of interest disclosure, a budget for their entire mandate, a well-defined roadmap with tangible objectives and deadlines.
2. **Treasury Custodians**: This is just a multisig to handle payments. Its members should not be part of the operatives or the leader. The custodians have the responsibility of keeping funds safe and ensuring the leader follows the scheduled budget.
3. **Dev, BD, and Comms Operatives**: Rather than having distinct sub-DAOs, each working on its own, we can simplify things and have people working together directly to get stuff done quickly. These people can apply directly to the leader or on the forum. The leader should include their salary in the budget request.

This structure would account for a total of 6 operative people and 5-7 custodians with signing duties only, reducing costs for the network and streamlining efficiency.

#### Ensuring transparency and accountability

One of the biggest accomplishments of The Charter was the great transparency and accountability; we certainly don't want to lose it. That's why I strongly recommend keeping some of the previous policies but also giving up on some business-killing ones:

- All discussions and meetings should happen in public on Discord whenever possible.
- If there is an internal private meeting, it should be communicated over the appropriate channels.
- Allow private speaking with other projects and potential businesses.
- All decisions should be taken through DAO proposals.
- The leader should report back to the community at least every 2 weeks about progress and goals.

#### How to practically create this

1. Post a governance proposal to Juno gov defining the terms of leader elections.
2. Proceed with leader election.
3. Find volunteers to join as treasury custodians.
4. Rename the council to "treasury custodians" and add the people through a gov vote.
5. Find people willing to work for the operatives' role. In an ideal world, the leader already has a team or a set of trusted people to work with who can be scrutinized by the community.
6. Create a new DAO with all the operatives and the leader inside.

### Tokenomics

I wrote this in my previous post, and I'll write it again here. Juno tokenomics is not very sustainable; it works well only during peak markets where there is lots of demand for the token for pure speculation. We need to change it.

I see two possible roads - not sure which would fit best:

**Option A: PSS LFG**

1. Drop the validator set and adopt PSS from the Hub.
2. Remove inflation.
3. Allocate a percentage of the community pool as "governance rewards."
4. Allow people to vote in governance directly or via governors.

**Option B: NO PSS**

1. Keep the current validator set.
2. Reduce inflation - or remove it but allocate a fixed amount from the community pool to it.
3. Forget the 12 years' plan.
4. Do not distribute staking rewards proportionally but rather based on validator position in the set. The less VP a validator has, the more staking rewards they should get.
5. Use quadratic voting for votes proxied by validators.

In both these options, we should probably fork out core-1 vesting and prop 16 funds.

### Juno Core

It's currently in a poor state; in the past 6 months, it only got security upgrades and minor version bumps. We should get back on track with it: bump to SDK 50, collaborate with Skip for Slinky and other cool implementations. While it's important to focus on dApps, the core should not be neglected, or you will become obsolete very quickly.

### Internal dAPPs

No one will save Juno. No one will ever build anything because Juno is cool. Devs build on a chain in two cases only:

- The blockchain itself is in a mega-hype moment, full of projects and people. Launching here is easy, and as a dev, I get an immediate profit by doing so. Not the Juno case.
- The blockchain itself is rich and can bribe devs to build, usually with oversized funding. Not the Juno case.

We have been in both these statuses, but those times are officially gone.

So what can we do? Build dApps ourselves. Having a suite of basic dApps made by the "Juno team" for Juno and owned by the community is crucial in the current phase of the network.

We need to show the cool features offered by Juno, by demonstrating that stuff can be built and successful. It needs to start with us.

How? Part of the dev operatives must be CW Devs. Some external help might be requested through RFPs.

## Am I still bullish?

Always. But it's getting frustrating to see such huge potential wasted, and the more time passes, the more drastic measures have to be taken.
