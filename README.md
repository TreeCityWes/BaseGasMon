# Coinbase Base Layer-2 Gas Fee Monitor by TreeCityWes

## Overview

The Coinbase Base Layer-2 Gas Fee Monitor is a simple Python script to track real-time Ethereum gas fees on Coinbase's Base Layer-2 Network. It utilizes Web3.py and an QuickNode URL to fetch the current gas price and base fee per gas. This information is displayed on the console with a time-stamp.

## Features

- Real-time tracking of gas prices in Gwei.
- Displays base fee per gas if EIP-1559 is supported.
- Easily configurable poll interval to fetch updated data.
- Uses the Web3.py library for a seamless and easy-to-understand implementation.

## Requirements

- Python 3.x
- Web3.py library
- An QuickNode URL or equivalent service to connect to the Ethereum network

## Installation

First, clone the repository to your local machine:

\```bash
git clone https://github.com/TreeCityWes/Coinbase-Base-Layer-2-Gas-Fee-Monitor.git
\```

Navigate into the project directory:

\```bash
cd Coinbase-Base-Layer-2-Gas-Fee-Monitor
\```

Install the necessary Python package:

\```bash
pip install web3
\```

## Usage

1. Update the `QuickNode_url` variable in the Python script with your QuickNode URL or equivalent service URL.

\```python
QuickNode_url = 'Your_QuickNode_URL_Here'
\```

2. Run the script:

\```bash
python main.py
\```

This will start the monitoring process, and you'll see real-time gas fee updates in the console.

## Configuration

You can set the `poll_interval` parameter in the `track_gas_price(poll_interval)` function to change how often the script fetches updated data. The default is set to 5 seconds.

## Contribution

Feel free to contribute by opening issues or submitting pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Credits

Created and maintained by [TreeCityWes](https://github.com/TreeCityWes).

## Disclaimer

This script is provided "as-is" and should be used for informational purposes only. Always perform your own due diligence before making any cryptocurrency transactions. We are not responsible for any losses incurred as a result of using this script.

## Contact

For more information, reach out to TreeCityWes on [Github](https://github.com/TreeCityWes) or [Twitter](https://twitter.com/TreeCityWes).
