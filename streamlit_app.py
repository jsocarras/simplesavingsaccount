import streamlit as st
from pytezos.client import PyTezosClient
import time

# --- Configuration ---
GHOSTNET_NODE = "https://ghostnet.smartpy.io"
# Your successfully deployed contract address
CONTRACT_ADDRESS = "KT1EKGH8Wa8FsoHsoeLaLg6QqXskRyoPpmqn"

# --- PyTezos Client ---
# Initialize a client for reading data without a key
pytezos_client = PyTezosClient().using(shell=GHOSTNET_NODE)

def get_contract_storage():
    """Fetches the current storage (the 'value') of the contract."""
    try:
        contract = pytezos_client.contract(CONTRACT_ADDRESS)
        storage = contract.storage()
        return storage
    except Exception as e:
        return f"Error fetching storage: {e}"

def call_contract_entrypoint(private_key, entrypoint, amount):
    """Calls a contract entrypoint to modify the storage."""
    try:
        client_with_key = PyTezosClient().using(shell=GHOSTNET_NODE, key=private_key)
        contract = client_with_key.contract(CONTRACT_ADDRESS)
        
        if entrypoint == "increment":
            op = contract.increment(amount)
        elif entrypoint == "decrement":
            op = contract.decrement(amount)
        else:
            return "Error: Invalid entrypoint specified."

        # 1. Send the operation, which returns an OperationGroup object (opg)
        opg = client_with_key.bulk(op).send()
        
        st.toast(f"Transaction sent! Waiting for confirmation...")
        
        # 2. Pass the ENTIRE 'opg' object to the wait function.
        client_with_key.wait(opg, min_confirmations=1)
        
        # 3. Now that we've waited, we can get the hash to display to the user.
        op_hash = opg.hash()
        
        return f"✅ Success! Tx Hash: [{op_hash}](https://ghostnet.tzkt.io/{op_hash})"

    except Exception as e:
        if "balance is too low" in str(e):
            return "🔥 Error: The account balance is too low to pay for the transaction fees."
        elif "invalid private key" in str(e) or "invalid checksum" in str(e):
             return "🔥 Error: The private key you entered is invalid. Please check it."
        return f"🔥 Error: {e}"

# --- Streamlit UI ---
st.set_page_config(page_title="Tezos Counter dApp", layout="wide")

st.title("Tezos Counter dApp")
st.write(f"Interact with a simple counter smart contract on the Tezos Ghostnet.")
st.write(f"**Contract Address:** `{CONTRACT_ADDRESS}`")

st.markdown("---")

st.header("Current Counter Value")
with st.spinner("Fetching value from the blockchain..."):
    current_value = get_contract_storage()
    if isinstance(current_value, str) and "Error" in current_value:
        st.error(current_value)
    else:
        st.metric(label="Value", value=str(current_value))
    
if st.button("Refresh Value"):
    st.rerun()

st.markdown("---")

st.header("Modify Counter Value")
st.warning("️**Security Warning:** This requires your private key. Don't have one? use: edskS1j4zsMjzYwU3syjzSn2FWf4st4g9Wyamd6fKkqfFmSZCpGAvLu2VpEDaK2Rr22qs5F3Gc9TYLJ1m6Br6b974uQyuGyy6x.")

private_key_input = st.text_input("Enter your Ghostnet account private key:", type="password", help="Don't have one? Use: 'edsk...'.")
amount_input = st.number_input("Enter amount:", min_value=1, value=1)

col1, col2 = st.columns(2)

def handle_transaction(entrypoint, amount):
    if not private_key_input:
        st.error("Please enter your private key.")
    else:
        with st.spinner("Sending transaction..."):
            result = call_contract_entrypoint(private_key_input, entrypoint, amount)
            st.markdown(result)
            if "Success" in result:
                st.toast("Success! Refreshing state...")
                time.sleep(1) # A short delay for a better user experience
                st.rerun()

with col1:
    if st.button("Increment", use_container_width=True):
        handle_transaction("increment", amount_input)

with col2:
    if st.button("Decrement", use_container_width=True):
        handle_transaction("decrement", amount_input)