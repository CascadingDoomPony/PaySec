from django.core.management.base import BaseCommand, CommandError
from polaris.models import Asset

from stellar_sdk import Keypair

class Command(BaseCommand):
    help = 'Generate new asset'

    """def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)"""

    def handle(self, *args, **options):
        issuer = Keypair.random()
        distributor = Keypair.random()

        with open("secretKeys.txt", "w") as f:
            f.write(f"{issuer.secret}\n{distributor.secret}")

        Asset.objects.create(
            code="TEST",
            issuer=issuer.public_key,
            distribution_seed=distributor.secret,
            sep6_enabled=True,
            sep24_enabled=True,
            deposit_enabled=True,
            withdrawal_enabled=True,
            symbol="$"
        )


