import json
from django.core.management.base import BaseCommand
from smartgrid_api.models import GridRow

class Command(BaseCommand):
    help = 'Import grid rows from grille_audit_stellantis.json into the database.'

    def handle(self, *args, **options):
        with open('grille_audit_stellantis.json', encoding='utf-8') as f:
            data = json.load(f)
        anomalies = data['grille_audit']['anomalies']
        GridRow.objects.all().delete()
        for anomaly in anomalies:
            points = anomaly.get('points_controles', {})
            GridRow.objects.create(
                category=anomaly.get('categorie', ''),
                anomalie=anomaly.get('description', ''),
                chapitre=anomaly.get('chapitre', ''),
                code_anomalie=str(anomaly.get('code_amadeus', '')),
                um='',
                uc='',
                ums='',
                bl='',
                aviexp='',
                info_sup='',
                um_enabled=points.get('UM', False),
                uc_enabled=points.get('UC', False),
                ugs_enabled=points.get('UMS', False),  # changed from ums_enabled
                bl_enabled=points.get('BL', False),
                avexp_enabled=points.get('AVIEXP', False),  # changed from aviexp_enabled
            )
        self.stdout.write(self.style.SUCCESS('Grid imported from JSON successfully.'))
