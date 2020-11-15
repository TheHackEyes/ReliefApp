# This is the relief app python page

#This is our initial state (values stored and maintained on blockchain by our smart contract).
# S = state object initiated as a HASH and any new keys in this variable default to 0.
#Smart Contract state

S = Hash(default_value=0)

#This runs when our contract is created on the blockchain, and never again.
@construct
def seed():
    #Gave myself 100 tokens!
    S['me'] = 100


# This method will be exported so our users can call it
@export
def transfer(amount: int, receiver: str):
    # ctx.caller is the verified identity of the person who signed this transaction
    # we will keep this reference as the "sender" of the transaction
    sender = ctx.caller

    # get the sender's balance from State
    balance = S[sender]

    # Assert the sender has the appropriate balance to send
    # If this assert fails the method will fail here
    # All values revert and no more code is executed
    assert balance >= amount, "Transfer amount exceeds available token balance"

    # subtract the tokens from the sender's balance
    S[sender] -= amount

    # add tokens to the receiver's balance
    S[receiver] += amount

    