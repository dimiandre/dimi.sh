# One Year Later on Juno

Hello! I'm Dimi 🦙. For those who don't know me, I helped found Juno, contributing to its launch phase with my protocols and engineering abilities. This note is a sequel to [my previous one](https://google.com), released now more than one year ago.

## What happened

After my article Juno went to a massive re-organization, a group of volunteer from the community proposed [The Charter](https://www.mintscan.io/juno/proposals/319) and it went live shortly after.

To summarize, The Charter is a combination of various sub-daos of the Juno Network that has the objective to enhance transparency and manage the chain in all of its aspects, including: operations, comunications and development.

It took some months to have it up and running, with public elections, lots of people involved and many discussions within the community. It went fully operative only in ~January 2024.

In the past 6 months of the charter, Juno reached a level of decentralizations and transparency like never before, accomplished the clearance of previous agreements and worked to define a budget to spend for the chain growth.

But, all this decenetralization and transparacency quickly highlighted the inefficiencies of the charter itself. It was taking weeks even to make the simpliest decision, with a super long burocratic and tiring process for everyone.

Because of this slowness, the Charter wasn't able to deliver enough to the juno community, basically focusing only on organizing the charter itself rather than driving the network to a new direction.

The charter now is going to be disbanded, with [this proposal](https://www.mintscan.io/juno/proposals/350). With my personal stake, and my validator company too, I voted NO to it because I though the best path forward would have been to fix the charter inefficiencies and keep working with the great people that have contributed so much to it. Unfortunately the prop passed, so now we need to think about something new.

## Today

Most of the Charter department members took proposal 350 literally, and immediately removed themselves from the various DAOs, effectively locking treasury and tokens in smart contracts that are now impossible to access without a software upgrade or admin onchain proposals. Additionaly, the proposal was bad worded and I can't see a way to continue the delegation program without putting at risk the 10M JUNO tokens in the hands of few people.

As of today, no one is effectively managing the chain. There is no roadmap. There is no objective. It's chaos.

This may sound tragic, but it can also be a huge opportuninty to restart and try again with something new, learning from the mistakes made down the road.

And no worries - I'll keep working on Juno Core as I always did since genesis. Yes I was here when reece was here, I was here when the frey was here, I was here when notional was here, and so on. So we are covered at least with basic upgrades and security patches.

## Next

This is the most fun part, because we can do something to quickly make thing up and running again, this time hopefully with a solid solution that can last a long time.

I think the next steps should be

1. Define a new more efficient organizational structure
2. Revisit tokenomics, locked balances, vestings, inflation, governance
3. Cleanup Juno Core code and write the necessary upgrades
4. Build dAPPs internally

Let's takle each of this one by one.

### New structure

What was really missing in the charter was someone giving direction to it, someone taking responsibility of decision. The whole charter idea was based on the fact that departments whould have done check and balances to the other, but in the real word that doesn't happen. Human collaboration requires leadrship to not get stuck.

A structure that may be efficient is the following

![Juno Structure](https://dimi.sh/img/juno-structure.png)

1. _Juno Leader_: This should be elected by the community. Anyone should be able to apply as a leader, and every mandate should be 6-12 months long. To apply a leader has to provide the following: Previous experience with juno, conflict of interest disclosure, a budget for its entire mandate, a well defined roadmap with tangible objectives and deadlines.
2. _Treasury Custodians_: This is just a multisig to handle payments. Its members should not be part of the operatives or the leader. The custodians have the responsibility of keeping funds safe and ensuring the leader is following the scheduled budget.
3. _Dev, BD and Comms Operatives_: Rather than having distinct subdaos each of those working by their own, we can simplify things and have people working together directly to get stuff done quickly. These people can apply directly to the leader or on the forum. The leader should include their salary in the budget request.

This structure would account for a total of 6 operative people and 5-7 custodians with signing duties only, reducing costs for the network and streamlining efficiency.

#### Ensuring transparency and accountability

One of the biggest accomplishments of the Charter was the great transparency and accountability, we certantly don't want to loose it. That's why I strongly reccomend to keep some of the previous policies, but also giving up on some business killing ones

- All discussions and meetings should happen in public on discord whenever possible
- If there is an internal private meeting, it should be communicated over the appropriate channels
- Allow private speaking with other projects and potential businesses.
- All the decisions should be taken trough daodao proposals
- The leader should report back to the community at least every 2 weeks about progress and goals

#### How to practically create this

1. Post a governance proposal to juno gov defining the terms of leader elections
1. Proceed with leader election
1. Find volunteers to join as treasury custodians
1. Rename the council to "treasury custodians" and add the people trough a gov vote
1. Find people willing to work for the operatives role. In an ideal world, the leader already has a team or a set of trusted people to work with that can be scrutined by the community.
1. Create a new dao with all the operatives and leader inside

### Tokenomics

I wrote this also in my previous post, and I'll writ it again here. Juno tokenomics is not very sustainable, it works well only during peak markets where there is lots of demand for the token for pure speculation. We need to change it.

I see two possible roads - not sure which would fit best

_Option A: PSS LFG_

1- Drop the validator set and adopt PSS from the Hub
2- Remove inflation
3- Allocate a percentage of the community pool as "goverance rewards"
4- Allow people to vote in governance directly or via governors.

_Option B: NO PSS_

1- Keep the current validator set
2- Reduce inflation - or remove it but allocate a fixed amount from community pool to it
3- Fuck off the 12 years bullshit
3- Not distribute staking rewards proportionally but rather based on validator position in the set. The less vp a validator has the more staking rewards should get.
4- Use quadratic votings for votes proxed by validators

In both this options we should probably fork out core-1 vestings and prop 16 funds.

### Juno Core

It's currently in a shitty looking face, in the past 6 months it only got security upgrades and minor version bumps. We should get back in track with it: bump to sdk 50, collaborate with skip for slinky and the other cool implementations. While it's important to focus on dapps, also the core should not be just left over or you will became obsolete very quickly

### Internal dAPPs

No one will save Juno. No one will ever build anything because juno is cool. Devs build on a chain in two cases only:

- The blockchain itself is in a mega-hype moment, it's full of projects and people. Launching here is easy and as dev I get an immediate profit by doing so. Not the juno case.
- The blockchain itself is rich af and can bribe devs to build, usually with oversized fundings. Not juno case.

We have been in both these statuses, but that times are officially gone.

So what can we do? Build dAPPs by ourselves. Having a suite of basic dAPPs made by "Juno team" for Juno and owned by the community is crucial in the current phase of the network.

We need to show the cool features offered by Juno, by demonstrating that stuff can be build and stuff can be successfull. It needs to start from us.

How? Part of the dev operatives must be CW Devs. Some external help might be requested trough RFPs.

## Am I still bullish?

Always. But it's getting frustrating to see such a huge potential wasted, and the more time it passes the more drastic measures has to be taken.
