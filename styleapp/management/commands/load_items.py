from django.core.management.base import BaseCommand
from styleapp.models import Items
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Items.objects.all().delete()
        f = open('items.json')
        items_list = json.load(f)
        for items in items_list['data']:
            name_ext = items.get('name')
            prodId_ext = int(items.get('id'))
            assetType_ext = int(items.get('assetType'))
            description_ext = int(items.get('description'))
            creatorName_ext = items.get('creatorName')
            price_ext = items.get('price')

            item_obj = Items.objects.create(
                name = name_ext,
                productId = prodId_ext,
                assetType = assetType_ext,
                description = description_ext,
                creatorName = creatorName_ext,
                price = price_ext,
            )

            print(item_obj.name + ' has been uploaded')

    # def handle(self, *args, **options):
    #     Items.objects.all().delete()
    #     f = open('items.json')
    #     items_list = json.load(f)
    #     for item in items_list:
    #         key_ext = items_list[champion]["key"]
    #         attack_ext = items_list[champion]["info"]["attack"]
    #         defense_ext = items_list[champion]["info"]["defense"]
    #         magic_ext = items_list[champion]["info"]["magic"]
    #         difficulty_ext = items_list[champion]["info"]["difficulty"]
    #         hp_ext = items_list[champion]["stats"]["hp"]
    #         hpperlevel_ext = items_list[champion]["stats"]["hpperlevel"]
    #         mp_ext = items_list[champion]["stats"]["mp"]
    #         mpperlevel_ext = items_list[champion]["stats"]["mpperlevel"]
    #         movespeed_ext = items_list[champion]["stats"]["movespeed"]
    #         armor_ext = items_list[champion]["stats"]["armor"]
    #         armorperlevel_ext = items_list[champion]["stats"]["armorperlevel"]
    #         spellblock_ext = items_list[champion]["stats"]["spellblock"]
    #         spellblockperlevel_ext = items_list[champion]["stats"]["spellblockperlevel"]
    #         attackrange_ext = items_list[champion]["stats"]["attackrange"]
    #         hpregen_ext = items_list[champion]["stats"]["hpregen"]
    #         hpregenperlevel_ext = items_list[champion]["stats"]["hpregenperlevel"]
    #         mpregen_ext = items_list[champion]["stats"]["mpregen"]
    #         mpregenperlevel_ext = items_list[champion]["stats"]["mpregenperlevel"]
    #         crit_ext = items_list[champion]["stats"]["crit"]
    #         critperlevel_ext = items_list[champion]["stats"]["critperlevel"]
    #         attackdamage_ext = items_list[champion]["stats"]["attackdamage"]
    #         attackdamageperlevel_ext = items_list[champion]["stats"]["attackdamageperlevel"]
    #         attackspeedperlevel_ext = items_list[champion]["stats"]["attackspeedperlevel"]
    #         attackspeed_ext = items_list[champion]["stats"]["attackspeed"]
    #         image_full_ext = items_list[champion]["image"]["full"]
    #         # print(key_ext)

    #         Champions.objects.create(
    #             key = key_ext,
    #             name = champion,
    #             attack = attack_ext,
    #             defense = defense_ext,
    #             magic = magic_ext,
    #             difficulty = difficulty_ext,
    #             hp = hp_ext,
    #             hpperlevel = hpperlevel_ext,
    #             mp = mp_ext,
    #             mpperlevel = mpperlevel_ext,
    #             movespeed = movespeed_ext,
    #             armor = armor_ext,
    #             armorperlevel = armorperlevel_ext,
    #             spellblock = spellblock_ext,
    #             spellblockperlevel = spellblockperlevel_ext,
    #             attackrange = attackrange_ext,
    #             hpregen = hpregen_ext,
    #             hpregenperlevel = hpregenperlevel_ext,
    #             mpregen = mpregen_ext,
    #             mpregenperlevel = mpregenperlevel_ext,
    #             crit = crit_ext,
    #             critperlevel = critperlevel_ext,
    #             attackdamage = attackdamage_ext,
    #             attackdamageperlevel = attackdamageperlevel_ext,
    #             attackspeedperlevel = attackspeedperlevel_ext,
    #             attackspeed = attackspeed_ext,
    #             image = image_full_ext,
    #         )            
                