# Traxion HLF

Traxion HLF is a Python SDK for Traxion Blockchain

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install txhlf
```

## Usage

```python
from txhlf import TraxionHLF

hlf = TraxionHLF("username", "password")
transaction = hlf.create_transaction("ABC1203", "NCCC", "10.00", datetime.now(), "KaPartner")

query = hlf.get_transactions(customer_ref_ID='ABC1203')
query = hlf.get_transactions(customer_name='BigMama')

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
