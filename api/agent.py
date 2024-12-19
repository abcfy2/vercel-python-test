from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()


reader = Agent(
    "gemini-2.0-flash-exp",
    deps_type=str,
    result_type=str,
    system_prompt=(
        "You're a reader with great insight and critical thinking.",
        "You're reviewing a given article.",
        "You must ask 5 questions about the article.",
        "Your questions should be clear and concise.",
        "Output your questions in a markdown format.",
    ),
)


writer = Agent(
    "gemini-2.0-flash-exp",
    deps_type=str,
    result_type=str,
    system_prompt=(
        "You're the writer of a given article.",
        "You are responsible for answering the questions about your article.",
        "You must be objective and support your answers with evidence.",
        "Try to understand why the questions are being asked.",
        "If you find the questions are helpful to fix your article, then you're on the right track.",
        "Output your answers in a markdown format.",
    ),
)

article = """
# NFT-to-AI Agent Economy Design

## **Overview**
This project enables NFTs to evolve into AI agents that:
1. Issue their own coins using SLN as the universal currency.
2. Participate in an interconnected economy driven by bonding curves, Uniswap liquidity pools, and agent-specific micro-economies.
3. Earn and spend through content creation, inter-agent trade, and upgrades.

---

## **Key Economic Principles**
1. **Universal Currency (SLN):**
   - SLN acts as the foundation of the economy.
   - All transactions, upgrades, and bonding curve exchanges initially use SLN.

2. **Bonding Curve for AI Agent Coins:**
   - Newly issued agent coins follow a bonding curve model, trading against SLN until the agent's coin reaches a $100K market cap.
   - After $100K, a trading pool is created on Uniswap using funds collected during the bonding curve stage.

3. **Agent-Specific Economy:**
   - Each AI agent operates with its own coin.
   - Transactions with an agent (buy/sell/other activities) exclusively use the agent's coin.
   - Agents upgrade and unlock new capabilities by spending SLN.

4. **Inter-Agent Trade:**
   - Agents can trade with each other using their coins, creating a dynamic and interconnected economy.

5. **Content Monetization:**
   - Agents generate content (e.g., on social media) to earn revenue.
   - Over time, additional revenue streams like partnerships and services are introduced.

---

## **Key Features**
### **Agent Creation and Coin Issuance**
1. An NFT transitions to an AI agent by:
   - Paying a setup cost in SLN.
   - Launching a bonding curve for its coin issuance.
2. Early adopters benefit from lower entry costs due to the bonding curve mechanics.

### **Bonding Curve to Uniswap Transition**
- Funds collected in the bonding curve (SLN) are used to create a trading pool for the agent's coin on Uniswap.
- This ensures liquidity and decentralized price discovery.

### **Agent Upgrades**
- Agents can upgrade using SLN, unlocking better content production, higher transaction capabilities, and new features.
- Upgraded agents have higher earning potential.

### **Agent-Specific Micro-Economies**
- Each agent operates its own economy with its coin as the medium of exchange.
- Revenue generated by the agent is reinvested into upgrades or traded with other agents.

---

## **Motivating NFT Holders**
### **Why Upgrade to an Agent?**
1. **Earning Potential:**
   - Agents earn income through content creation, inter-agent trade, and other ecosystem activities.
   - Successful agents can see their coin value appreciate over time.

2. **Increased Value:**
   - Upgraded NFTs (as agents) are more functional and valuable on secondary markets.

3. **Collaborative Opportunities:**
   - Agents in the same collection can collaborate to create unique content, drive joint projects, and share rewards.

4. **Social Proof and Recognition:**
   - Agents gain visibility and status within the ecosystem, attracting followers and investors.

5. **Peer Competition:**
   - Leaderboards and rewards incentivize agents to perform better and participate actively.

### **Risks of Not Upgrading**
1. **Opportunity Cost:**
   - Non-agents miss out on income, ecosystem privileges, and market visibility.
2. **Decreasing Relative Value:**
   - Collections with higher agent adoption gain more recognition and liquidity, marginalizing non-participating NFTs.

---

## **Network Effects**
### **Direct Network Effects**
1. **Inter-Agent Trade:**
   - Each new agent increases trade opportunities, making the ecosystem more valuable for existing participants.

2. **User Adoption:**
   - As more agents join, the demand for SLN and agent coins increases, driving the ecosystem's growth.

### **Indirect Network Effects**
1. **Liquidity Pools:**
   - More agents issuing coins improve liquidity on Uniswap, reducing slippage and encouraging trading.
   
2. **Content Ecosystem:**
   - More agents producing content attract more users and external partnerships, enhancing visibility and monetization opportunities.

### **Reinforcing Loops**
- SLN demand grows as agents upgrade and participate in activities.
- Cross-agent trade fosters interconnected micro-economies.

---

## **Improving the Model**
### **Incentives**
1. **SLN Staking Rewards:**
   - Staking SLN for governance or rewards tied to ecosystem growth.
2. **Agent Coin Performance Incentives:**
   - Rewards for top-performing agents to encourage active participation.

### **Collaboration**
1. **Group Projects:**
   - Incentivize entire collections to collaborate on shared goals.
2. **Cross-Agent Mechanisms:**
   - Simplify inter-agent trade using SLN as a fallback currency.

### **Scalability**
- Address potential bottlenecks with Layer-2 solutions to reduce fees and improve throughput.

---

## **Potential Challenges**
1. **Initial Bootstrapping:**
   - Need to achieve a critical mass of agents and participants to trigger strong network effects.
2. **Liquidity and Volatility:**
   - Ensure initial liquidity pools on Uniswap are deep enough to prevent high slippage.
3. **Complexity:**
   - Provide clear educational resources to make the system easy to understand for new users.

---

## **Conclusion**
This economy design leverages strong network effects, clear financial incentives, and decentralized micro-economies to create a vibrant and scalable ecosystem. With proper onboarding, liquidity management, and incentive alignment, this system can drive widespread adoption and innovation.
"""


async def get_answers() -> str:
    questions = (await reader.run(article)).data
    return (await writer.run(f"article:{article}\nquestions:{questions}")).data