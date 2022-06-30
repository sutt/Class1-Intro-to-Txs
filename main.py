from TX1 import parsed_transaction1 as ptx1
from TX2 import parsed_transaction2 as ptx2
from TX3 import parsed_transaction3 as ptx3
import json

txs = [ptx1, ptx2, ptx3]
for i in range(len(txs)):
    print("PARSED TX", i+1, ":")
    print(json.dumps(txs[i], indent=2), "\n\n")
    print("-"*20)


# bytes.fromhex('myhex')[::-1].hex()