from django.db import models

# Create your models here.

# super user
# yking19
# Imgoingin@20


class RK_Ashram_marg(models.Model):
    
    id = models.AutoField(primary_key=True)
    Tree_code = models.CharField(max_length=8, unique=True, null=False, error_messages ={ 
                    "unique":"The Tree code you have entered is already exists."
                    } )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    common_name = models.CharField(max_length=45, null=False)
    scientific_name = models.CharField(max_length=45)
    Age = models.IntegerField(null=False)
    Height = models.FloatField(null=False)
    Diameter_girth = models.FloatField(null=False)
    closest_address = models.CharField(max_length=45, null=False)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6,
                                 unique=True, null=False, 
                                 error_messages={"unique" : "Longitude value already exists"})
    Latitude = models.DecimalField(max_digits=8, decimal_places=6,
                                 unique=True, null=False, 
                                 error_messages={"unique" : "Latitude value already exists"})
    specie_code = models.CharField(max_length=8)
    condition = models.CharField(max_length=45)

    def __unicode__(self):
        return self.id

class Mandir_marg(models.Model):
    id = models.AutoField(primary_key=True)
    Tree_code = models.CharField(max_length=8)
    common_name = models.CharField(max_length=45)
    
    def __unicode__(self):
        return self.id



# @event.listens_for(Akbar_Road, 'before_insert')
# def before_insert_function(mapper, connection, target):
#         # 'target' is your object
#         target.common_name
#         target.specie_code
#         target.scientific_name = specie_names.get(str(target.common_name))
#         target.specie_code = specie_codes.get(str(target.common_name))


# @event.listens_for(Akbar_Road, 'before_update')
# def before_update_function(mapper, connection, target):
#         # 'target' is your object
#         target.common_name
#         target.specie_code
#         target.scientific_name = specie_names.get(str(target.common_name))
#         target.specie_code = specie_codes.get(str(target.common_name))









#_____________botanical and specie code auto fill________________

specie_names = {'Peepal'                         : 'Ficus_religiosa',
                'Bargad'                         : 'Ficus_benghalensis',
                'Amaltas'                        : 'Cassia_fistula',
                'Gulmohar'                       : 'Delonix_regia',
                'Arjun'                          : 'Terminalia_arjuna',
                'Drum_Stick'                     : 'Moringa_oleifera',
                'Semal'                          : 'Bombax_ceiba',
                'Safeda'                         : 'Eucalyptus',
                'Scholar_tree'                   : 'Alstonia_scholaris',
                'Neem'                           : 'Azadirachta_indica',
                'Bakayan'                        : 'Melia_azedarach',
                'False_ashoka'                   : 'Polyalthia_longifolia',
                'Pilkhan'                        : 'Ficus_virens',
                'Sausage_tree'                   : 'Kigelia_africana',
                'Sentang'                        : 'Azadirachta_excelsa',
                'Kikar'                          : 'Acacia_nilotica',
                'Weeping_bottelbrush'            : 'Melaleuca_viminalis',
                'Mango'                          : 'Mangifera_indica',
                'Mulberry'                       : 'Morus',
                'Palm'                           : 'Arecaceae',
                'Jamun'                          : 'Syzygium_cumini',
                'Royal_palm'                     : 'Roystonea_regia',
                'Maharukh'                       : 'Ailanthus_excelsa',
                'Jungle_jalebi'                  : 'Pithecellobium_dulce',


                'Unknown'                        : 'Unknown',

                None                             : 'Default'
               }

specie_codes = {'Peepal'                                 : 1621,
                'Bargad'                                 : 1622,
                'Amaltas'                                : 1321,
                'Gulmohar'                               : 1421,
                'Arjun'                                  : 2121,
                'Drum_Stick'                             : 1921,
                'Semal'                                  : 1221,
                'Safeda'                                 : 1521,
                'Scholar_tree'                           : 1021,
                'Neem'                                   : 1121,
                'Bakayan'                                : 1821,
                'False_ashoka'                           : 2021,
                'Pilkhan'                                : 1623,
                'Sausage_tree'                           : 1721,
                'Sentang'                                : 1122,
                'Kikar'                                  : 1010,
                'Weeping_bottelbrush'                    : 1008,
                'Mango'                                  : 1003,
                'Mulberry'                               : 1004,
                'Royal_palm'                             : 1005,
                'Jamun'                                  : 1006,
                'Maharukh'                               : 1007,
                'Jungle_jalebi'                          : 1008,


                'Unknown'                                : 1001,
                None                                     : 'Default'
               }


