#from importlib.metadata import distribution
from django.core.management.base import BaseCommand, CommandError
import toml
from pathlib import Path

class Command(BaseCommand):
    help = 'Generate a TOML for a new asset'

    """def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)"""

    def add_arguments(self, parser):  # pragma: no cover
        self.command_parser = parser
        self.command_parser.add_argument(
            "--asset-code", "-i", help="The code of the asset"
        )
        self.command_parser.add_argument(
            "--signing-key", "-d", help="The key that signs the transactions on the asset"
        )


    def handle(self, *args, **options):
        asset_code = options.get("asset_code")
        signing_key = options.get("signing_key")
        toml_dict = {"SIGNING_KEY": f"{signing_key}",
                    "TRANSFER_SERVER": "http://localhost:8000/sep6",
                    "TRANSFER_SERVER_SEP0024": "http://localhost:8000/sep24",
                    "WEB_AUTH_ENDPOINT": "http://localhost:8000/auth",
                    "KYC_SERVER": "http://localhost:8000/kyc",
                    "DIRECT_PAYMENT_SERVER": "http://localhost:8000/sep31",
                    "ANCHOR_QUOTE_SERVER": "http://localhost:8000/sep38",
                    "CURRENCIES": [{"code": f"{asset_code}",
                                    "issuer": f"{signing_key}"}],
                    "Documentation": {"Sample": "Sample"}
                    
        }
        #toml_string = toml.dumps(toml_dict)  # Output to a string

        output_file_name = Path("server/static/polaris/local-stellar.toml")
        with open(output_file_name, "w") as toml_file:
            toml.dump(toml_dict, toml_file)


