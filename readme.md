# Run command: python3 -m streamlit run 1_numbercounter.py


# Interactive Tezos Smart Contract Boilerplate

This project provides an interactive, educational tool for understanding a basic Tezos smart contract. It uses Streamlit to create a user-friendly interface that walks you through the code, explains its core concepts, and allows you to simulate its behavior directly in your browser.

This application is the perfect starting point for developers new to Tezos and SmartPy, offering a hands-on approach to learning the fundamentals of decentralized application (dApp) development.

## 🚀 Features

*   **Full Code Display**: View the complete Python code for a "Counter" smart contract written in SmartPy.
*   **Detailed Explanations**: Each section of the smart contract is broken down and explained to clarify its purpose and function.
*   **Interactive Simulation**: A live simulation lets you call the contract's `increment` and `decrement` functions and see the state change in real time.
*   **Educational Focus**: Designed to teach the core concepts of Tezos smart contracts, including storage, entrypoints, and state management.
*   **Guidance for Next Steps**: Offers suggestions for expanding the boilerplate into more complex and feature-rich dApps.

## 📋 Getting Started

Follow these instructions to get the application running on your local machine.

### Prerequisites

You will need to have Python 3.7 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository (or download the code)**:
    If you have this project in a Git repository, clone it:
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```
    Alternatively, save the Python code from the Streamlit app into a file named `app.py`.

2.  **Install the necessary Python package**:
    This application requires the Streamlit library. Install it using pip:
    ```bash
    pip install streamlit
    ```

## ▶️ How to Run the Application

Once you have installed the prerequisites, you can run the application with a single command:

```bash
streamlit run app.py
```
Your web browser will automatically open a new tab with the running application.
## 🧠 The Smart Contract Explained
The boilerplate included in this application is a simple "Counter" contract written in SmartPy, a Python-based language for Tezos.

- Storage: The contract maintains a single piece of data: an integer named count. This represents the contract's state on the Tezos blockchain.
- Entrypoints: The contract has two functions, or entrypoints, that users can call to interact with it:
- increment(value): Increases the count by a specified value.
- decrement(value): Decreases the count by a specified value.
- Initialization: When the contract is deployed, its count is set to an initial value. In our simulation, it starts at 0.

## 💡 Next Steps
After you feel comfortable with this boilerplate, you can use it as a foundation for more sophisticated projects. Consider exploring the following enhancements:

- Access Control: Modify the contract to only allow specific Tezos addresses (users) to call its entrypoints.
- Complex Data Structures: Instead of a simple integer, use more complex data types like maps or lists to store more structured information. For example, you could create a contract where each user has their own personal counter.
- Token Standards: Learn about and implement Tezos token standards like FA2 (the equivalent of ERC-721/1155) to create your own non-fungible tokens (NFTs) or fungible tokens.
- Inter-Contract Calls: Build a dApp where your smart contract can interact with other contracts already deployed on the Tezos blockchain.
- For more in-depth learning, refer to the official Tezos Developer Portal and the SmartPy documentation.

## 📄 License
This project is open-source and available under the MIT License.
