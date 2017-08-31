from django.core.management.base import BaseCommand, CommandError
import csv
from datetime import datetime
from facturier.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open("export_facturier.csv","rb") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            csvreader.next()
            for row in csvreader:
                tit, customer, status, creation_date, update_date, product, price, qty = row

                for col in row:
                    # if tit[0]=="F":
                    #     if status=='STANDBY':
                    #         date = datetime.strptime(creation_date, "%d/%m/%y %H:%M")
                    #         Facture.objects.get_or_create(title=tit, status="1", date_facturation=date)
                    #
                    #     elif status=='PAID':
                    #         date_fac = datetime.strptime(creation_date, "%d/%m/%y %H:%M")
                    #         date_val= datetime.strptime(update_date, "%d/%m/%y %H:%M")
                    #
                    #         Facture.objects.get_or_create(title=tit, status="2", date_facturation=date_fac, date_validation=date_val)

                    if tit[0]=="D":
                        if status == "LOST":

                            date_cre = datetime.strptime(creation_date, "%d/%m/%y %H:%M")
                            date_ref = datetime.strptime(update_date, "%d/%m/%y %H:%M")

                            new_client = Client.objects.get_or_create(name = "cc", prenom='new')

                            devis = Devis.objects.get_or_create(title=tit,  status="refuse", client=new_client, date_creation=date_cre, date_update=date_ref),

                            LigneDevis.objects.get_or_create(descpt=product, prix=price, qty=qty, devis=devis)

                        elif status == "STANDBY":
                            date_cre = datetime.strptime(creation_date, "%d/%m/%y %H:%M")

                            new_client, _  = Client.objects.get_or_create(name = "cc", prenom='new')

                            devis = Devis.objects.get_or_create(title=tit,  status="progress", client=new_client, date_creation=date_cre)
                            
                            LigneDevis.objects.get_or_create(descpt=product, prix=price, qty=qty, devis=devis)
