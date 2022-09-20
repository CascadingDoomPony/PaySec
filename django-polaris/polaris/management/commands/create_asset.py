from django.core.management.base import BaseCommand, CommandError
from polaris.models import Asset

from stellar_sdk import Keypair

class Command(BaseCommand):
    help = 'Generate new asset'

    """def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)"""

    def add_arguments(self, parser):  # pragma: no cover
        self.command_parser = parser
        self.command_parser.add_argument(
            "--issuer-seed", "-i", help="the issuer's secret key"
        )
        self.command_parser.add_argument(
            "--distribution-seed", "-d", help="the distribution account's secret key"
        )


    def handle(self, *args, **options):
        issuer = Keypair.from_secret(
            options.get("issuer_seed")
        )
        distributor = options.get("distribution_seed")

        Asset.objects.create(
            code="PYSC",
            issuer=issuer.public_key,
            distribution_seed=distributor,
            sep6_enabled=True,
            sep24_enabled=True,
            deposit_enabled=True,
            withdrawal_enabled=True,
            symbol="$"
        )
        print(f"Created Asset issuer: {issuer.public_key}, distributer {distributor}")


