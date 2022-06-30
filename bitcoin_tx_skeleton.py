# Basic Structure of any Legacy Bitcoin Transaction
# {
# Version: (4 bytes, little endian),
# Input Count: (Compact Size),
# Input(s): [
#     {
#     TXID: (32 bytes, little endian)
#     VOUT: (4 bytes, little endian)
#     ScriptSig Size: (Compact Size)
#     ScriptSig: (unlocking script, big endian)
#     Sequence: (4 bytes)
#     }
# ],
# Output Count: (Compact Size)
# Output(s):
#     Amount: (8 bytes, sats value, little endian)
#     ScriptPubKey Size: (Compact Size)
#     ScriptPubKey: (locking script, big endian)
# Locktime: (4 Bytes, little endian)
# }



# python dict format you should use

parsed_transaction = {
    "version": 0,
    "input_count": 1,
    "inputs": [
        {
            "txid": '',
            "vout": 0,
            "scriptSig": '',
            "sequence": 0,
        },
    ],
    "output_count": 1,
    "outputs": [
        {
            "amount": 0,
            "scriptPubKey": ''
        },
    ],
    "locktime": 0
}