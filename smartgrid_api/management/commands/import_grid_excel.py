import pandas as pd
from django.core.management.base import BaseCommand
from smartgrid_api.models import GridRow

class Command(BaseCommand):
    help = 'Import grid rows from grille_audit_stellantis.xlsx into the database.'

    def handle(self, *args, **options):
        df = pd.read_excel('grille_audit_stellantis.xlsx', header=None)
        # Trouver la ligne d'en-tête
        header_row = None
        for i, row in df.iterrows():
            if row.astype(str).str.contains('Anomalie', case=False).any():
                header_row = i
                break
        if header_row is None:
            self.stdout.write(self.style.ERROR("Header row with 'Anomalie' not found."))
            return
        # Relire avec la bonne ligne d'en-tête
        df = pd.read_excel('grille_audit_stellantis.xlsx', header=header_row)
        df.columns = [str(c).strip().replace('\n', ' ').replace('  ', ' ') for c in df.columns]
        # Détection dynamique des colonnes
        col_map = {}
        for col in df.columns:
            c = col.lower().replace(' ', '')
            if 'anomalie' in c: col_map['anomalie'] = col
            if 'chapitre' in c: col_map['chapitre'] = col
            if 'code' in c and 'amadeus' in c: col_map['code_anomalie'] = col
            if c == 'um': col_map['um'] = col
            if c == 'uc': col_map['uc'] = col
            if c == 'ums': col_map['ums'] = col
            if c == 'bl': col_map['bl'] = col
            if 'aviexp' in c: col_map['aviexp'] = col
            if 'libellé' in c or 'libelle' in c: col_map['libelle'] = col
        anom_col = col_map.get('anomalie')
        libelle_col = col_map.get('libelle')
        if not anom_col:
            self.stdout.write(self.style.ERROR("Colonne 'Anomalie' non trouvée."))
            return
        stop_idx = df[df[anom_col].astype(str).str.contains('Usine|Emetteur|UR|Réf Docinfo|Version|Date de création', na=False)].index
        if not stop_idx.empty:
            df = df.loc[:stop_idx[0]-1]
        GridRow.objects.all().delete()
        for _, row in df.iterrows():
            def is_enabled(val):
                # Si la cellule est vide ou NaN, c'est gris (désactivé)
                return not (pd.isna(val) or str(val).strip() == '' or str(val).strip().lower() == 'nan')
            # Use the label (libellé) as the anomaly name if present, else fallback to 'anomalie' column
            anomalie_value = row.get(libelle_col, '') if libelle_col else row.get(col_map.get('anomalie'), '')
            GridRow.objects.create(
                anomalie=anomalie_value,
                chapitre=row.get(col_map.get('chapitre'), ''),
                code_anomalie=row.get(col_map.get('code_anomalie'), ''),
                um=row.get(col_map.get('um'), ''),
                uc=row.get(col_map.get('uc'), ''),
                ums=row.get(col_map.get('ums'), ''),
                bl=row.get(col_map.get('bl'), ''),
                aviexp=row.get(col_map.get('aviexp'), ''),
                info_sup='',
                um_enabled=is_enabled(row.get(col_map.get('um'))),
                uc_enabled=is_enabled(row.get(col_map.get('uc'))),
                ums_enabled=is_enabled(row.get(col_map.get('ums'))),
                bl_enabled=is_enabled(row.get(col_map.get('bl'))),
                aviexp_enabled=is_enabled(row.get(col_map.get('aviexp'))),
            )
        self.stdout.write(self.style.SUCCESS('Grid imported successfully.'))
