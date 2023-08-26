from web3 import Web3
import asyncio
from datetime import datetime

QuickNode_url = '(Insert QuickNode URL)'
web3 = Web3(Web3.HTTPProvider(QuickNode_url))

async def track_gas_price(poll_interval):
    while True:
        try:
            # Fetch current gas price
            gas_price = web3.eth.gas_price
            # Convert gas price from Wei to Gwei and round to 6 decimal places
            gas_price_gwei = round(web3.from_wei(gas_price, 'gwei'), 6)
            
            # Fetch recommended base fee if EIP-1559 is supported
            latest_block = web3.eth.get_block('latest')
            base_fee_per_gas = latest_block.get('baseFeePerGas', None)
            
            # Convert base fee from Wei to Gwei and round to 6 decimal places
            if base_fee_per_gas is not None:
                base_fee_gwei = round(web3.from_wei(base_fee_per_gas, 'gwei'), 6)
                base_fee_str = f"Base fee: {base_fee_gwei} Gwei"
            else:
                base_fee_str = ""

            # Get current time with seconds
            current_time = datetime.now().strftime("%I:%M:%S %p ET")

            # Format the output
            output = f"{current_time} - Gas Price on Base: {gas_price_gwei} Gwei --- {base_fee_str} - #StayXen with TreeCityWes"
            
            print(output)
        except Exception as e:
            print("Error occurred:", str(e))
        
        await asyncio.sleep(poll_interval)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(track_gas_price(5))

if __name__ == '__main__':
    main()
