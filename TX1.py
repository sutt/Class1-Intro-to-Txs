# This was the first ever bitcoin transaction where Satoshi sent Hal 10 BTC

txid = 'f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16'
raw_hex = '0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000'

'''
01000000
01
c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704
00000000
48
47304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901
ffffffff

02

00ca9a3b00000000
43
4104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac

00286bee00000000
43
410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac

00000000
'''
# Exercise: Parse the above TX by hand!

def hex_to_num(s_hex, little_endian=True):
    if (little_endian): s_hex = bytes.fromhex(s_hex)[::-1].hex()
    return int(s_hex, 16)
    
# python dict format you should use

parsed_transaction1 = {
    "version": hex_to_num('01000000'),
    "input_count": 1,
    "inputs": [
        {
            "txid": 'c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704',
            "vout": 0,
            "scriptSig": '4847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901',
            "sequence": hex_to_num('ffffffff', little_endian=False),
        },
    ],
    "output_count": 2,
    "outputs": [
        {
            "amount": hex_to_num('00ca9a3b00000000'),
            "scriptPubKey": '434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac'
        },
        {
            "amount": hex_to_num('00286bee00000000'),
            "scriptPubKey": '43410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac'
        },
    ],
    "locktime": 0
}

# import json
# pretty = json.dumps(parsed_transaction1, indent=2)
# print(pretty)

'''
{
  "version": 1,
  "input_count": 1,
  "inputs": [
    {
      "txid": "c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704",
      "vout": 0,
      "scriptSig": "4847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901",
      "sequence": 4294967295
    }
  ],
  "output_count": 2,
  "outputs": [
    {
      "amount": 1000000000,
      "scriptPubKey": "434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac"
    },
    {
      "amount": 4000000000,
      "scriptPubKey": "43410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac"
    }
  ],
  "locktime": 0
}
'''